# GithubHost
## 前言  
因为有几个域名被DNS污染了，GitHub老是看不见图，遂有了这个工程。虽然没大用是了。。。

## 广而告之  
现在主流浏览器基本上都支持基于HTTPS的DNS，很大程度上可以替代本项目。  
你可以根据实际情况进行选择。  

## 功能  
利用海外的机器进行相关网站的DNS查询, 将得到的结果发布到issue页面和release附件。  
+ 支持周期性自动发布
    + 每月1/16号发布issue
+ 支持自动回复  
    + 如果想查询最新的host，可以自己开个issue，自动回复。
    + 举例[issue #1](https://github.com/ButterAndButterfly/GithubHost/issues/1)
+ 支持通过http链接获取host文件  
    + 你可以通过以下的地址获取附件中的host文件
        + Github源地址:   <https://github.com/ButterAndButterfly/GithubHost/releases/download/v1/host.txt>
        + Github镜像: <https://hub.fastgit.org/ButterAndButterfly/GithubHost/releases/download/v1/host.txt>
    + host文件将由Github Actions机器人每天定时刷新，当有issue提交时也会触发构建
    + ps: 为啥不直接commit到仓库里，因为会更加冗余记录啊

## 查看
+ 请移步[issue](https://github.com/ButterAndButterfly/GithubHost/issues/)页面。   
+ 更改hosts后，注意`ipconfig /flushdns`刷新DNS缓存。

