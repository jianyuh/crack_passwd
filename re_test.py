import re    
    
text = "JGood is a handsome booy, he is cool, clever, and so on..."    
regex1 = re.match(r"\w*oo\w*", text)    
if regex1:    
    print "regex1:" , regex1  
    print "result1:" ,regex1.group(0)    
else:    
    print 'not match'  
print "\n"  
  
regex2 = re.compile(r'(\w*oo\w*)')  
print "result2:" , regex2.findall(text)  
print "\n"  
  
regex3 = re.compile(r'(\w*oo\w*).+?(\w*eve\w*).*')  
#print regex3.findall(text)
#print "\n"
regex3_result = regex3.search(text)  
if regex3_result:   
    print "regex3:", regex3  
    print " result3:",regex3_result.group(1)," ",regex3_result.group(2)  
else:  
    print 'not match'  
