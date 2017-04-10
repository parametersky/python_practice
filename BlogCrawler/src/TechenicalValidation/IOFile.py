import sys
reload(sys)
sys.setdefaultencoding('utf-8')

srcf = open("1.html","r")
content = srcf.read()
print srcf.encoding
print content;
testf = open("test.txt","w")
testf.write("test 1\n")
testf.write("stst")
testf.close()