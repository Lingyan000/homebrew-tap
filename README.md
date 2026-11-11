# FluxDO Homebrew tap

FluxDO 的 Homebrew Cask 仓库。

## 安装

首次包含 `fluxdo-package-managers.zip` 的 FluxDO 稳定版发布并同步后，可以执行以下命令。

```sh
brew install --cask Lingyan000/tap/fluxdo
```

## 更新

Cask 声明 `auto_updates true`，应用内可通过 Sparkle 更新。使用 Homebrew 更新时执行以下命令。

```sh
brew update
brew upgrade --cask --greedy fluxdo
```

## 清单同步

GitHub Actions 每六小时检查 [FluxDO 最新稳定版](https://github.com/Lingyan000/fluxdo/releases/latest)，
下载 `fluxdo-package-managers.zip` 及其 SHA-256 文件，校验后同步 `Casks/fluxdo.rb`。
也可在 Actions 中手动运行 **Sync FluxDO release**。

首次包含清单的版本发布前，同步任务正常结束，等待后续发布。
工作流使用本仓库的 `GITHUB_TOKEN` 写入更新。
