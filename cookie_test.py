#!/usr/bin/python  
# coding:utf-8   
import httplib2  
import urllib2  
import re #正则表达式模块  
  
class PageClass:  
  
    #获取指定url的网页内容  
    def get_page(self,url,headers):  
        http=httplib2.Http()  
        response,content=http.request(url,'GET',headers=headers)  
        #return content.decode('unicode-escape').encode('utf-8')  
        return content.decode('unicode-escape').encode('utf-8')  
          
def main():              
    headers={"cookie":'your cookie'}  
    url = 'http://fengchao.baidu.com'  
    #print headers  
    page = PageClass()  
    content = page.get_page(url,headers)  
    print content  
  
if __name__ == "__main__":  
    main()  
