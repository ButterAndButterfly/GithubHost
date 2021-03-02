#!/usr/bin/env python
# coding:utf-8
 
import socket, time

domains = [
    'api.github.com',
    'assets-cdn.github.com',
    'avatars.githubusercontent.com',
    'avatars0.githubusercontent.com',
    'camo.githubusercontent.com',
    'cloud.githubusercontent.com',
    'codeload.github.com',
    'favicons.githubusercontent.com',
    'gist.github.com',
    'gist.githubusercontent.com',
    'github.com',
    'github.githubassets.com',
    'marketplace-screenshots.githubusercontent.com',
    'octocaptcha.com',                                      # 用途包括但不限于: 创建organization时的验证码
    'raw.githubusercontent.com',
    'repository-images.githubusercontent.com',
    'uploads.github.com',                                   # 用途包括但不限于: release附件上传
    'user-images.githubusercontent.com',
]

def gen_host():
    for domain in domains:
        print('Querying ip for domain %s'%domain)
        ip = socket.gethostbyname(domain)
        print(ip)
        yield (ip, domain)
        
def get_now_date_str(format_string="%Y-%m-%d %H:%M:%S"):#"%Y-%m-%d %H:%M:%S"
    time_stamp = int(time.time())
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date

def output_hosts():
    with open('hosts.txt', 'w') as f:
        f.write('```\n')
        f.write('# GitHub Start \n')
        f.write('# Last update at %s (Machine Local Time)\n'%(get_now_date_str()))
        for ip, domain in gen_host():
            f.write('%s %s\n'%(ip, domain))
        f.write('# GitHub End \n')
        f.write('```\n')
if __name__ == '__main__':
    output_hosts()
