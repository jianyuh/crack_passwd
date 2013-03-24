#!/usr/bin/python  
# -*-coding:utf-8 -*-  


import HTMLParser  
import urllib  
import sys  
  
#定义HTML解析器  
class parseLinks(HTMLParser.HTMLParser):  
    #该方法用来处理开始标签的，eg:<div id="main">  
    def handle_starttag(self, tag, attrs):  
        if tag == 'a':  #如果为<a>标签  
            #name为标签的属性名，如href、name、id、onClick等等  
            for name,value in attrs:      
                if name == 'href': #这时选择href属性  
                    print "name_value: ",value  #href属性的值  
                    print "first tag:",self.get_starttag_text() #<a>标签的开始tag  
                    print "\n"  
  
if __name__ == "__main__":  
    #创建HTML解析器的实例  
    lParser = parseLinks()  
    #打开HTML文件  
    fs = open("test.html","w")
    fs.write(urllib.urlopen("http://www.baidu.com").read())
    lParser.feed(urllib.urlopen("http://www.baidu.com").read())  
    lParser.close()  
