#!/usr/bin/env python
# coding:utf-8
 
import socket
from datetime import datetime, timedelta, timezone
domains = [
    'github.com',
    'githubapp.com',
    'api.github.com',
    'raw.github.com',
    'gist.github.com',
    'octocaptcha.com',                                      # 用途包括但不限于: 创建organization时的验证码
    'help.github.com',
    'live.github.com',
    'github.community',
    'githubstatus.com',
    'pages.github.com',
    'status.github.com',
    'uploads.github.com',                                   # 用途包括但不限于: release附件上传
    'nodeload.github.com',
    'training.github.com',
    'codeload.github.com',
    'assets-cdn.github.com',
    'github.githubassets.com',
    'documentcloud.github.com',
    'raw.githubusercontent.com',
    'gist.githubusercontent.com',
    'camo.githubusercontent.com',
    'cloud.githubusercontent.com',
    'media.githubusercontent.com',
    'github-com.s3.amazonaws.com',
    'github.global.ssl.fastly.net',
    'desktop.githubusercontent.com',
    'github-cloud.s3.amazonaws.com',
    'avatars.githubusercontent.com',
    'favicons.githubusercontent.com',
    'avatars0.githubusercontent.com',
    'avatars1.githubusercontent.com',
    'avatars2.githubusercontent.com',
    'avatars3.githubusercontent.com',
    'avatars4.githubusercontent.com',
    'avatars5.githubusercontent.com',
    'avatars6.githubusercontent.com',
    'avatars7.githubusercontent.com',
    'avatars8.githubusercontent.com',
    'customer-stories-feed.github.com',
    'user-images.githubusercontent.com',
    'repository-images.githubusercontent.com',
    'marketplace-screenshots.githubusercontent.com',
    'github-production-user-asset-6210df.s3.amazonaws.com',
    'github-production-release-asset-2e65be.s3.amazonaws.com',
    'github-production-repository-file-5c1aeb.s3.amazonaws.com',
]

        
def get_ip_list(domain): # 获取域名解析出的IP列表
  ip_list = []
  try:
    addrs = socket.getaddrinfo(domain, None)
    for item in addrs:
      if item[4][0] not in ip_list:
        ip_list.append(item[4][0])
  except Exception as e:
    ip_list.append('No resolution for '+domain)
    pass
  return ip_list

def gen_host():
    for domain in domains:
        print('Querying ip for domain %s'%domain)
        list = get_ip_list(domain)
        for ip in list:
            yield (ip, domain)
        

def get_now_date_str(format_string="%Y-%m-%d %H:%M:%S"):#"%Y-%m-%d %H:%M:%S"
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    str_date = bj_dt.strftime(format_string)
    return str_date

def output_hosts():
    with open('hosts.txt', 'w') as f:
        f.write('```\n')
        f.write('# GitHub Start \n')
        f.write('# Last update at %s (Beijing Time)\n'%(get_now_date_str()))
        for ip, domain in gen_host():
            print('ip %s'%ip)
            f.write('%s %s\n'%(ip, domain))
        f.write('# GitHub End \n')
        f.write('```\n')
if __name__ == '__main__':
    output_hosts()
