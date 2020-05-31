# GithubHost
## 前言  
因为有几个域名被DNS污染了，GitHub老是看不见图，遂有了这个工程。虽然没大用是了。。。

## 功能  
利用海外的机器进行相关网站的DNS查询, 将得到的结果发布到issue页面。  
+ 支持周期性自动发布
    + 每月1/16号发布issue
+ 支持自动回复  
    + 如果想查询最新的host，可以自己开个issue，自动回复。
    + 举例[issue #1](https://github.com/ButterAndButterfly/GithubHost/issues/1)

## 查看
+ 请移步[issue](https://github.com/ButterAndButterfly/GithubHost/issues/)页面。   
+ 更改hosts后，注意`ipconfig /flushdns`刷新DNS缓存。

