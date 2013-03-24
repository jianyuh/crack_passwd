#!/usr/bin/python  
# -*-coding:utf-8 -*-  

#http://blog.csdn.net/lianxiang_biancheng/article/details/7772487\
#http://stackoverflow.com/questions/3334809/python-urllib2-how-to-send-cookie-with-urlopen-request


"""
http://stackoverflow.com/questions/3334809/python-urllib2-how-to-send-cookie-with-urlopen-request

import urllib2
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'cookiename=cookievalue'))
f = opener.open("http://example.com/")

"""
"""
import urllib2
import urllib
from cookielib import CookieJar
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# input-type values from the html form
formdata = { "username" : username, "password": password, "form-id" : "1234" }
data_encoded = urllib.urlencode(formdata)
response = opener.open("https://page.com/login.php", data_encoded)
content = response.read()
"""

"""
>>> cookies = dict(cookies_are='working')

>>> r = requests.get('http://httpbin.org/cookies', cookies=cookies)
>>> r.text
'{"cookies": {"cookies_are": "working"}}'
"""

"""
    def loginByCookie(self, cookie_path):
        with open(cookie_path) as fp:
            cookie_str = fp.read()
            cookie_dict = dict([v.split('=', 1) for v in cookie_str.strip().split(';')])
            self.session.cookies = requests.utils.cookiejar_from_dict(cookie_dict)

        self.getToken()

    def saveCookie(self, cookie_path):
        with open(cookie_path, 'w') as fp:
            cookie_dict = requests.utils.dict_from_cookiejar(self.session.cookies)
            cookie_str = '; '.join([k + '=' + v for k, v in cookie_dict.iteritems()])
            fp.write(cookie_str)
"""


import httplib2  
import urllib2  
import re #正则表达式模块  
  
class WeiboClass: #定义一个weibo类  
  
    #获取指定url的网页内容  
    def get_content(self,url,headers,idname):  
        http=httplib2.Http()  
        response,content=http.request(url+idname,'GET',headers=headers)  
        #print url+str(id)  
        return content.decode('unicode-escape').encode('utf-8')  
  
    #判断weibo的用户是否是企业用户  
    def is_company(self,url,headers,id):  
        content=self.get_content(url,headers,id)  
        title=r'行业'  
        company_title=re.compile(title)   
        if company_title.search(content): #使用正则表达式对title进行匹配          
            return 1  
        else:  
            return 0  
          
    #获取用户的weibo信息：ID，主页url，昵称  
    def get_info(self, url,headers,id):  
        #flag=self.is_company(url,headers,id)  
        flag = 0
        print flag
        content=self.get_content(url,headers,id)  
        f = open('test.html','w')
        f.write(content)

        print content
        print "come to judge point"
        if flag==0:  #如果用户是个人用户              
            #print content  
            #微博ID  
            id_flag=r'\$CONFIG\[\'oid\'\] = \'([0-9].+?)\';'  
            #id_flag=r'([0-9].+)'  
            #$CONFIG['oid'] = '1249021097';
            id_re=re.compile(id_flag)  
            id_regx=id_re.search(content)  
            #print id_regx
            id=id_regx.group(1)  
            print id  
""" 
            #微博url  
            url_flag=r'<meta http-equiv="mobile-agent" content="format=xhtml;" url="weibo.cn/(.+?)\?'  
            url_re=re.compile(url_flag)  
            url_regx=url_re.search(content)  
            print url_regx
            url_0=url_regx.group(1)  
            url='http://weibo.com/'+url_0  
            print url  
"""           
"""
            #昵称  
            name_flag='<div class="name clearfix">.+?<div class="left">(.+?)<'  
            name_re=re.compile(name_flag,re.S)  
            name_regx=name_re.search(content)  
            name=name_regx.group(1)  
            name=name.decode('utf-8').encode('GBK')  
            print name  
""" 
def main():              
    headers={"cookie":'[SINAGLOBAL=1984971985220.9092.1359180451713;__utma=15428400.693373649.1359180927.1359180927.1359180927.1;__utmz=15428400.1359180927.1.1.utmcsr=weibo.com|utmccn=(referral)|utmcmd=referral|utmcct=/traits;ssoln=huangjy91%40sina.com;sso_info=ln%3Dhuangjy91%2540sina.com%26nick%3Dhuangjy91%26uid%3D1249021097;un=huangjy91@sina.com;wvr=5;SUE=es%3D9545c125c985641a803f24b8d77fc489%26ev%3Dv1%26es2%3Db305e0b67d46f7ba1a92930259592134%26rs0%3DQxI5ZquyoNwhKmAxCQbZ8m3TpXPWqF7y8vmaUMUFRvfQgJTg%252B3PCmq9OT96QkpBLeFV%252F32HH%252Fm%252FNb2LP8pD8CNW1hgWtf%252FSRXnUhAAn7D8MECNKFSOKzPD%252FjpOZdXInjikIfz%252F1bBo8EA%252Bj5BlBK%252FIVCDcAVP0no0IdMntTw8oo%253D%26rv%3D0;SUP=cv%3D1%26bt%3D1364113956%26et%3D1364200356%26d%3Dc909%26i%3D5100%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D1249021097%26user%3Dhuangjy91%26ag%3D2%26name%3Dhuangjy91%2540sina.com%26nick%3Dhuangjy91%26fmp%3D%26lcp%3D;SUS=SID-1249021097-1364113956-JA-vk8bi-f8b9f9b14319ff51f6fbf8d77f5b29a4;ALF=1364285862;SSOLoginState=1364113956;_s_tentry=login.sina.com.cn;Apache=8518323497846.723.1364113972255;ULV=1364113972450:34:14:2:8518323497846.723.1364113972255:1364108043308;USRUG=usr413119;USRHAWB=usr313110;UOR=,weibo.com,login.sina.com.cn#video.sina.com.cn;SinaRot/u/1249021097%3Fwvr%3D5%26=94'}      
    url='http://weibo.com/'  
    print headers  
    page = WeiboClass()  
    page.get_info(url,headers,'pennyliang')  
  
  
if __name__ == "__main__":  
    main()  
