
import urllib2;
import urllib;
import re;
url = "http://restapi.amap.com/v3/assistant/coordinate/convert?locations="
para = "&coordsys=gps&output=xml&key=82c0eeeb24c552b89b04f974389f0727"

f = open("coordinates.txt","r")
fo = open("reusltCor.txt","w")
longtitude = 118.783648
latitude = 31.893504

while True:
    latitude = f.readline().strip('\n')
    longtitude = f.readline().strip('\n')
    if longtitude:
        urls = url+str(longtitude)+","+str(latitude)+para
        print urls+"\n"
        response = urllib2.urlopen(urls);
        content =  response.read().decode('utf-8')
        print content+"\n"
        pattern = re.compile('<locations>(.*?),(.*?)</locations>',re.S)
        result = re.findall(pattern,content)
        for item in result:
            fo.write(str(latitude)+", "+ str(item[1])+"\n")
            fo.write(str(longtitude)+", "+ str(item[0])+"\n")
    else:
        break;
