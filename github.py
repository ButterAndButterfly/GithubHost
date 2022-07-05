#!/usr/bin/env python
# coding:utf-8
import os
import requests,json
from datetime import datetime, timedelta, timezone
import socket_query

class GithubHelper:
    
    def __init__(self, owner, repo, auth, **args):
        self.auth = auth
        self.owner = owner
        self.repo = repo
        
    def getLatestRelease(self, **args):
        url = 'https://api.github.com/repos/%s/%s/releases/latest'%(self.owner, self.repo)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.auth}
        res = requests.get(url, headers=headers).json()
        #print(res)
        return res
    
                
    def updateReleaseBody(self, release_id, body, **args):
        url = 'https://api.github.com/repos/%s/%s/releases/%d'%(self.owner, self.repo, release_id)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.auth}
        param = {
            "body": body
        }
        res = requests.request("PATCH", url, data=json.dumps(param), headers=headers).json()
        #print(res)
        return res 
        
    def updateReleaseAsset(self, asset_id, name, **args):
        url = 'https://api.github.com/repos/%s/%s/releases/assets/%d'%(self.owner, self.repo, asset_id)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.auth}
        param = '{"name":"%s"}'%name
        res = requests.request("PATCH", url, data=param, headers=headers).json()
        #print(res)
        return res    
            
    def deleteReleaseAsset(self, asset_id, **args):
        url = 'https://api.github.com/repos/%s/%s/releases/assets/%d'%(self.owner, self.repo, asset_id)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.auth}
        res = requests.request("DELETE", url, headers=headers)
        #print(res.text)
        return res
        
    def uploadReleaseAsset(self, release_id:int, name, data, **args):
        url = 'https://uploads.github.com/repos/%s/%s/releases/%d/assets?name=%s'%(self.owner, self.repo, release_id, name)
        headers = {'content-type': 'application/octet-stream', 'Accept': 'application/vnd.github.v3.+json', "Authorization": "token "+ self.auth}
        res = requests.request("POST", url, data=data, headers=headers).json()
        #print(res)
        return res
        
    def replaceLatestReleaseAssets(self, name, data, **args):
        if not "releaseInfo" in locals():
            releaseInfo = self.getLatestRelease()
        release_id = releaseInfo['id']
        assets = releaseInfo['assets']
        # 删除原来的附件
        for asset in assets:
            if name == asset["name"]:
                self.deleteReleaseAsset(asset['id'])
                break;
        # 上传新的附件
        return self.uploadReleaseAsset(release_id, name, data)
        
    def shaGithubFile(path):
        url = 'https://api.github.com/repos/%s/%s/contents/%s'%(self.owner, self.repo, path)
        headers = {'Accept': 'application/vnd.github.v3.star+json', "Authorization": "token "+ self.auth}
        res = requests.get(url, headers=headers).json()
        return res["sha"] if "sha" in res else None
        
    def downloadGithubFile(path):
        url = 'https://raw.githubusercontent.com/%s/%s/master/%s'%(self.owner, self.repo, path)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.star+json', "Authorization": "token "+ self.auth}
        res = requests.get(url, headers=headers)
        return res.content
        
    def uploadGithubFile(data:bytes, path):
        sha = shaGithubFile(path, token)
        print(sha)
        url = 'https://api.github.com/repos/%s/%s/contents/%s'%(self.owner, self.repo, path)
        headers = {'User-Agent': 'None', 'Accept': 'application/vnd.github.v3.star+json', "Authorization": "token "+ token}
        def gen():
            yield (r'{"message":"Updated at %d.",'%int(time.time()*1000)).encode("utf-8")
            if sha:
                yield (r'"sha":"%s",'%sha).encode("utf-8")
            yield r'"content":"'.encode("utf-8")
            yield base64.b64encode(data)
            yield r'"}'.encode("utf-8")
        res = requests.put(url, data = gen(), headers=headers)
        print(res.text)
        return res
        
def get_now_date_str(format_string="%Y-%m-%d %H:%M:%S"):#"%Y-%m-%d %H:%M:%S"
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    str_date = bj_dt.strftime(format_string)
    return str_date
    
def load_from_env():
    repo_full_name = os.environ.get('MY_REPOSITORY')
    owner = os.environ.get('MY_OWNER')
    repo = repo_full_name[len(owner) + 1:]
    token = os.environ.get('MY_GITHUB_TOKEN')
    github_config = {
        "repo": repo,
        "owner": owner,
        "auth": token,
    }
    return github_config

     
if __name__ == "__main__":
    github_config = load_from_env()
    '''
    github_config = {
        "repo": "repo",
        "owner": "owner",
        "auth": "auth",
    }
    '''
    date_now = get_now_date_str()
    lines = []
    lines.append('# GitHub Start')
    lines.append('# from https://github.com/ButterAndButterfly/GithubHost')
    lines.append('# Last update at %s (Beijing Time)'%date_now)
    for ip, domain in socket_query.gen_host():
        lines.append("%s %s"%(ip, domain))
    lines.append('# GitHub End')
    data = '\n'.join(lines)
    
    helper = GithubHelper(**github_config)    
    release_info = helper.getLatestRelease()   
    result = helper.replaceLatestReleaseAssets(name = "host.txt", data = data, release_info=release_info)
    print(result)
    if "id" in result:
        body = \
        """
+ 你可以通过以下的地址获取附件中的host文件
    + Github源地址:   <https://github.com/ButterAndButterfly/GithubHost/releases/download/v1/host.txt>
    + Github镜像: <https://hub.fastgit.xyz/ButterAndButterfly/GithubHost/releases/download/v1/host.txt>
+ host文件将由机器人每天定时刷新，最后更新于(北京时间)：
        """
        body += date_now
        body = body.strip()
        helper.updateReleaseBody(release_id = release_info["id"], body=body)

