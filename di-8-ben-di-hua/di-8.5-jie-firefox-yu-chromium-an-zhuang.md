# 8.5 网络浏览器

## 火狐浏览器

### 安装普通版本（更新频繁）

- 使用 pkg 安装

```sh
# pkg install firefox
```

- 或者使用 Ports

```sh
# cd /usr/ports/www/firefox
# make install clean
```

### 安装长期支持版本

- 使用 pkg 安装

```sh
pkg install firefox-esr
```

- 或者使用 Ports

```sh
# cd /usr/ports/www/firefox-esr/
# make install clean
```

## Chromium

Chromium 不是 Chrome，但在 FreeBSD 中的启动命令为 `chrome`。

---

- 使用 pkg 安装

```sh
# pkg install chromium
```

- 或者使用 Ports

```sh
# cd /usr/ports/www/chromium
# make install clean
```

> **警告**
>
> 要编译 Chromium，你必须拥有至少 12G 内存，或等量的交换分区 + 内存。

## Chrome（Linux 兼容层）

- 使用 pkg 安装

```sh
# pkg install linux-chrome
```

- 或者使用 Ports

```sh
# cd /usr/ports/www/linux-chrome/ 
# make install clean
```

## 附录：Chromium 使用 Google 账号同步

>**技巧**
>
>有些项目认为目前移除的组件仍不够彻底，因此提供了 Port `www/ungoogled-chromium`。该软件移除了更多与谷歌相关的不透明组件。

- 由于是开源产物，Chromium 与 Google Chrome 的关系类似于 AOSP 与 Pixel UI 的关系。Chromium 无法直接从 Google Chrome 的在线插件商店下载安装插件，只能手动从本地安装 crx（同步启用后可自动同步浏览器插件）。Chromium 也不自带 Google 翻译插件等功能。更多差异可参见 [此网页](https://chromium.googlesource.com/chromium/src/+/master/docs/chromium_browser_vs_google_chrome.md)。
- 首先，`Chromium` 并非 `Google Chrome`，前者是 The Chromium Project 在 [BSD 3-Clause "New" or "Revised" License](https://github.com/chromium/chromium/blob/main/LICENSE) 下发布的开源与自由软件，后者是 Google LLC 的专有软件。

- Chromium 在 [Chromium 89](https://archlinux.org/news/chromium-losing-sync-support-in-early-march/) 发布后删除了之前自带的与 Chrome 同款的登录 Google 账号的默认 api。

在开始获取 token 之前，需要先加入以下两个 Google 邮件列表论坛：

- [Google browser sign-in test account](https://groups.google.com/u/0/a/chromium.org/g/google-browser-signin-testaccounts)
- [Chromium-dev](https://groups.google.com/a/chromium.org/g/chromium-dev)

![](../.gitbook/assets/join-chromium-dev-for-api1.png)

由于仅需 Chrome Google API 的访问权限，因此必须关闭这两个邮件列表的消息通知（即“不接收电子邮件”），否则可能会受到频繁的邮件轰炸。

![](../.gitbook/assets/join-chromium-dev-for-api2.png)

![](../.gitbook/assets/join-chromium-dev-for-api3.png)

加入 Google browser sign-in test account 群组后，你可能会看到：“您无权访问此内容”之类的提示，这很正常，无需担心。

![join-mail-list-for-google-api-error2](../.gitbook/assets/join-chromium--list-2error.png)

之后，用浏览器打开 [谷歌云控制台网站](https://console.cloud.google.com/)

>**注意**
>
>登录控制台时使用的谷歌账户必须与之前加入邮件列表的账户相同。

![](../.gitbook/assets/chromium-use-google-api-guide-0.png)

点击左上角的“My First Project”，然后在弹出窗口的右上角选择“新建项目”即可。

![](../.gitbook/assets/chromium-use-google-api-guide-02.png)

项目名称可随意填写，组织保持默认设置。

![](../.gitbook/assets/chromium-use-google-api-guide-03.png)

点击左上角的“My First Project”，然后在弹出窗口中选择你刚才创建的项目（此处我的是 google-sync）。

![](../.gitbook/assets/chromium-use-google-api-guide-04.png)

点击上图中的“API 和服务”，再点击“+ 启用 API 和服务”

![](../.gitbook/assets/chromium-use-google-api-guide-04-1.png)

搜索 'chrome-sync' 找到下列内容

![](../.gitbook/assets/chromium-use-google-api-guide-06.png)


点击启用“Chrome Sync API”

![](../.gitbook/assets/chromium-use-google-api-guide-05.png)

之后会在已启用的 API 和服务列表中显示下列状态

![](../.gitbook/assets/chromium-use-google-api-guide-07.png)

选择“OAuth 权限请求页面”：

![](../.gitbook/assets/chromium-use-google-api-guide-08.png)

创建外部应用：

![](../.gitbook/assets/chromium-use-google-api-guide-09.png)

![](../.gitbook/assets/chromium-use-google-api-guide-10.png)

![](../.gitbook/assets/chromium-use-google-api-guide-11.png)

![](../.gitbook/assets/chromium-use-google-api-guide-12.png)

创建后如图：

![](../.gitbook/assets/chromium-use-google-api-guide-13.png)

点击“客户端”，创建 OAuth 客户端 ID“，应用类型为“桌面应用”：

![](../.gitbook/assets/chromium-use-google-api-guide-14.png)

创建后如图：

![](../.gitbook/assets/chromium-use-google-api-guide-15.png)

点击创建的“桌面客户端 1”

![](../.gitbook/assets/chromium-use-google-api-guide-16.png)

我们获得了（这是笔者的，是无效的，读者必须自己生成自己的）:

- 客户端 ID `502882456359-okloi0a7k6vjodss69so97tmqmv0jjj5.apps.googleusercontent.com`
- 客户端密钥 `GoCSPX-iKHEKZmP4w_zdq0Z8nwOqz6SF2_M`

退回“API 和服务”，点击“+ 创建凭据”，再点击”API 密钥“。

![](../.gitbook/assets/chromium-use-google-api-guide-17.png)

我们就获得了一个 API 密钥（这是笔者的，是无效的，读者必须自己生成自己的）：`AIzaSyDVpYvJQUn9HTjAiD89y3xBDOG3oaxV5_E`

![](../.gitbook/assets/chromium-use-google-api-guide-18.png)

打开凭据概览一下：

![](../.gitbook/assets/chromium-use-google-api-guide-19.png)


编辑 `~/.profile`，加入（这是笔者的，是无效的，读者必须自己生成自己的）：

>**注意**
>
>本文仅在默认 shell sh 和 KDE 6 下测试通过。如果使用的环境不同，欢迎提交 PR。

```sh
export GOOGLE_API_KEY=AIzaSyDVpYvJQUn9HTjAiD89y3xBDOG3oaxV5_E  # 这里填 API 密钥
export GOOGLE_DEFAULT_CLIENT_ID=502882456359-okloi0a7k6vjodss69so97tmqmv0jjj5.apps.googleusercontent.com  # 这里填客户端 ID
export GOOGLE_DEFAULT_CLIENT_SECRET=GoCSPX-iKHEKZmP4w_zdq0Z8nwOqz6SF2_M  # 这里填客户端密钥
```

然后重启一下。再打开 Chromium。

点击“开启同步功能”：

![](../.gitbook/assets/chromium-use-google-api-guide-20.png)

输入你自己的账户：

![](../.gitbook/assets/chromium-use-google-api-guide-21.png)

输入你自己的账户密码：

![](../.gitbook/assets/chromium-use-google-api-guide-22.png)

![](../.gitbook/assets/chromium-use-google-api-guide-23.png)

查看同步情况：

![](../.gitbook/assets/chromium-use-google-api-guide-24.png)

### 参考文献

- [Chromium Sync - Learning to Pi](https://www.learningtopi.com/sbc/chromium-sync)
- [为 Chromium 恢复登录功能](https://nyac.at/posts/google-sync-in-chromium)


## 故障排除与未竟事宜

### 解决 Chromium 出现未知错误导致占用大量性能的问题

将参数添加到启动图标中（图标为文本文件）：

```sh
chrome --disk-cache-size=0 --disable-gpu
```

