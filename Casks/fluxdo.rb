cask "fluxdo" do
  arch arm: "arm64", intel: "x86_64"

  version "0.2.30"
  sha256 arm:   "7c92800139131fd4921f8dc81648399195dc76f7301cc79f506ab8c9d3b1f688",
         intel: "ef778da0e2e39e2ab0eecb8df428a8127480880da44189848b3a0e263cf8b506"

  url "https://github.com/Lingyan000/fluxdo/releases/download/v#{version}/fluxdo-macos-#{arch}.dmg"
  name "FluxDO"
  desc "Unofficial Linux.do community client"
  homepage "https://github.com/Lingyan000/fluxdo"

  auto_updates true
  depends_on macos: :monterey

  app "fluxdo.app"
end
