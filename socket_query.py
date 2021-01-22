#!/usr/bin/env python
# coding:utf-8
 
import socket

def output_hosts():
    domains = ['github.com',
                'gist.github.com',
                'assets-cdn.github.com',
                'raw.githubusercontent.com',
                'gist.githubusercontent.com',
                'cloud.githubusercontent.com',
                'camo.githubusercontent.com',
                'avatars0.githubusercontent.com',
                'avatars1.githubusercontent.com',
                'avatars2.githubusercontent.com',
                'avatars3.githubusercontent.com',
                'avatars4.githubusercontent.com',
                'avatars5.githubusercontent.com',
                'avatars6.githubusercontent.com',
                'avatars7.githubusercontent.com',
                'avatars8.githubusercontent.com',
                'avatars.githubusercontent.com',
                'github.githubassets.com',
                'user-images.githubusercontent.com',
                'codeload.github.com',
                'api.github.com']
    
    with open('hosts.txt', 'w') as f:
        f.write('```\n')
        f.write('# GitHub Start \n')
        for domain in domains:
            print('Querying ip for domain %s'%domain)
            ip = socket.gethostbyname(domain)
            print(ip)
            f.write('%s %s\n'%(ip, domain))
        f.write('# GitHub End \n') 
        f.write('```\n')
        
        
    
if __name__ == '__main__':
    output_hosts()
