#net.py
#@author imkh 
#modify by wuzeming 2019/3/29
import urllib.request
import random
import re
import subprocess
import json
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
]
url = "https://d.ishadowx.com/"
resp = urllib.request.Request(url)
resp.add_header('User-Agent', random.choice(user_agent))
res= urllib.request.urlopen(resp)
content = res.read()
content=content.decode('utf-8')#转化为utf-8

#pattern = re.compile('<div.*?col-sm-4 text-center">.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>.*?<font.*>.*?</h4>.*?<h4>(.*?)</h4>.*?</div>',re.S)
pattern = re.compile('<div.*?"hover-text">.*?<h4>IP(.*?)</span>.*?</h4>.*?<h4>(.*?)\n</span>.*?</h4>.*?<h4>(.*?)\n</span>.*?</h4>.*?<h4>(.*?)</h4>',re.S)
items = re.findall(pattern,content)
print(items)
pwd=[]
for i in items:
    pwd.append([i[0].split(">")[1],i[1].split(">")[1],i[2].split(">")[1],i[3].split(":")[1]])

'''
print(pwd)   
password1 = items[0][2].split(":")[1]#USA
password2 = items[1][2].split(":")[1]#HK
password3 = items[2][2].split(":")[1]#JP
#print(content)
print(password1)
print(password2)
print(password3)
'''
subprocess.call('taskkill /f /im shadowsocks.exe',stdout=subprocess.PIPE)
#更换为你的ss配置文件路径
ssconfigpath = "D:\Shadowsocks-4.1.5\gui-config.json"

#i为不同服务器 美国：0 1 新加坡：2 3 4 5 SSR：6 7  || 只有新加坡服务器能访问谷歌学术，其他被限制，原因不明

sever=4

with open(ssconfigpath,"r+") as f:
    data = json.load(f)
    data["configs"][0]["server"] = pwd[sever][0]
    data["configs"][0]["server_port"] = pwd[sever][1]
    data["configs"][0]["password"] = pwd[sever][2]
    data["configs"][0]["method"] = pwd[sever][3]
    f.seek(0)
    json.dump(data,f,indent=4)

#更改为你的ss程序路径
sspath = "D:\Shadowsocks-4.1.5\Shadowsocks.exe"
subprocess.Popen(sspath)
print("ok!")
