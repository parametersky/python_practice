
import urllib2;
import urllib;
#direct use url open to open a url
response = urllib2.urlopen("http://www.baidu.com");

# use request to open an url 
# request = urllib2.Request("http://www.baidu.com",data header);

# request = urllib2.Request("http://www.baidu.com");
# response = urllib2.urlopen(request);
# 
# print response.read();

import cookielib
cookie = cookielib.CookieJar();
handler = urllib2.HTTPCookieProcessor(cookie);
opener = urllib2.build_opener(handler);
# urllib2.install_opener(opener);
# response = urllib2.urlopen("http://www.baidu.com")
response = opener.open("http://www.baidu.com")
# print response.read()
for item in cookie:
    print 'Name = '+item.name;
    print 'Value = '+item.value;

