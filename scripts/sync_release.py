#!/usr/bin/env python3
"""Sync the Cask published with the latest stable FluxDO release."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile


REPOSITORY = "Lingyan000/fluxdo"
ARCHIVE = "fluxdo-package-managers.zip"


def main():
    release = json.loads(subprocess.check_output(
        ["gh", "api", f"repos/{REPOSITORY}/releases/latest"], text=True
    ))
    tag = release["tag_name"]
    if release["draft"] or release["prerelease"] or not re.fullmatch(r"v\d+\.\d+\.\d+", tag):
        raise ValueError("Expected a published stable release")
    assets = {asset["name"] for asset in release["assets"]}
    if ARCHIVE not in assets:
        print(f"{tag} has no package-manager manifests yet. Waiting for the first supported release.")
        return
    with tempfile.TemporaryDirectory() as directory:
        subprocess.run([
            "gh", "release", "download", tag, "--repo", REPOSITORY,
            "--pattern", ARCHIVE, "--pattern", ARCHIVE + ".sha256", "--dir", directory,
        ], check=True)
        archive = Path(directory) / ARCHIVE
        expected = Path(str(archive) + ".sha256").read_text().split()[0]
        if hashlib.sha256(archive.read_bytes()).hexdigest() != expected:
            raise ValueError("Release manifest checksum mismatch")
        with zipfile.ZipFile(archive) as source:
            content = source.read("homebrew/Casks/fluxdo.rb").decode("utf-8")
    version = tag[1:]
    if f'  version "{version}"' not in content:
        raise ValueError("Cask version does not match release tag")
    cask = Path(__file__).resolve().parents[1] / "Casks/fluxdo.rb"
    if cask.exists():
        previous = re.search(r'^  version "(\d+\.\d+\.\d+)"$', cask.read_text(), re.MULTILINE)
        if previous and tuple(map(int, previous[1].split("."))) > tuple(map(int, version.split("."))):
            raise ValueError("Refusing to downgrade the Cask")
    cask.parent.mkdir(exist_ok=True)
    cask.write_text(content)
    print(f"Synced FluxDO {version}")


if __name__ == "__main__":
    main()
