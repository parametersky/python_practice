# encoding=utf-8
import sys
import urllib
import urllib2
import Queue
import re
queue = Queue.Queue();


# get first page's blog list
reload(sys)
sys.setdefaultencoding('utf-8')
def getSinaBlogContent(url):
    print "url is "+ url;
    response  = urllib2.urlopen(url)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?class="articalTitle".*?>(.*?)</div>.*?<div.*?id="sina_keyword_ad_area2".*?>(.*?)</div>', re.S);
#     pattern = re.compile('<div id="module_920" .*?>(.*?)</div>', re.S);
    result = re.findall(pattern, content)
    if len(result) == 0:
        print "empty result";
        return None;
    else:
        return result[0];
    
# content contains two parts: title and body
def writeBlogContentToHtml(filename,content):
    print "write content:";
    print content;
    dest = open(filename,"wb");
    dest.write(content[0]);
    dest.write(content[1]);
    dest.close();
def wirteListToFile(filename,lst):
    dest = open(filename,"wb")
    for item in lst:
        dest.write(item[1]+" "+item[0]+" "+item[2]+"\n")
    dest.close();
        
def getFirstPageBlog():
    url = "http://blog.sina.com.cn/u/2144596567";
    response = urllib2.urlopen(url);
    content = response.read().decode('utf-8');
    # pattern = re.compile('<div.*?class="blog_title">.*?<a.*?>(.*?)</a>.*?</dev>.*?<span class="time SG_textc">.*?</span>',re.S);
    pattern = re.compile('<div id=.*? class="blog_title">.*?<a href=(.*?) target=.*?>(.*?)</a>.*?<span class="time SG_txtc">(.*?)</span>',re.S);
    result = re.findall(pattern, content)
    for item in result:
        print item[0] + " "+ item[1]+" "+item[2];
        queue.put((item[1],item[2],item[0]))
        list.append((item[1],item[2],item[0].replace('"', '')))
    print "done";
    for url in list:
        print url[0];
    content = getSinaBlogContent(list[0][2]);
    if content != None:
        writeBlogContentToHtml(filename = list[0][0]+".html",content = content);
PageTitle="http://www.court.gov.cn/cpwsw/sx/sxsyqszjrmfy/yxrmfy/ms/index_"
YQPageTitle="http://www.court.gov.cn/cpwsw/sx/sxsyqszjrmfy/yqscqrmfy/ms/index_"
iwant = [];
def getAllSegment():
    pages = 49
    for i in range(int(pages)):
        url = YQPageTitle+""+str(i+1)+".htm"
        getIContentFromUrl(url)
    dest = open("text.txt","wb")
    for item in iwant:
        dest.write(item+"\n")
    dest.close();
def getIContentFromUrl(url):
    print "url is "+ url;
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                         'Accept-Encoding': 'none',
                                'Accept-Language': 'en-US,en;q=0.8',
                                       'Connection': 'keep-alive'}
    req = urllib2.Request(url,headers=hdr)
    response = urllib2.urlopen(req)
    content = response.read().decode('utf-8')
    pattern = re.compile('<a.*?>(.*?)</a>', re.S);
#     pattern = re.compile('<div id="module_920" .*?>(.*?)</div>', re.S);
    result = re.findall(pattern, content)
    for item in result:
        iwant.append(item)



BlogListUrl = "http://blog.sina.com.cn/s/articlelist_2144596567_0_1.html"
BlogUrlHead = "http://blog.sina.com.cn/s/articlelist_2144596567_0_"
list = [];#list of blogs. blog contains (name, time, url)
def getAllBlogs(url):
    pages = getPages(BlogListUrl);
    print "pages is "+pages
    for i in range(int(pages)):
        url = BlogUrlHead+""+str(i+1)+".html"
        getBlogList(url);
    wirteListToFile("list.txt",list)
    i = len(list)
#     writeContentToHtml("BlogList.txt", list)
    reversed(list);
    while i > 0:
        blog = list[i-1]
        content = getSinaBlogContent(blog[2])
        if content != None:
            time = blog[1].replace("(", "").replace(")","").split(" ")[0].replace("-","_")
            writeBlogContentToHtml(time+" "+blog[0]+".html", content)
        i = i-1
    
    

def getBlogList(url):
    print "getBlogList in "+url
    result = getContentFromUrl(url, '<a title=\"(.*?)\" target="_blank" href=\"(.*?)\">.*?</a></span>.*?<span class="atc_tm SG_txtc">(.*?)</span>');
#     result = getContentFromUrl(url, '<a title=(.*?) target="_blank" href=(.*?)>.*?</a>')
    for item in result:
        list.append((item[0],item[2],item[1]));
    return list
    
    
def getPages(url):
#     response = urllib2.urlopen(url)
#     content = response.read().decode("utf-8")
#     pattern = re.compile('<div class="SG_page">.*?<span style=.*?>共(.*?)页</span>',re.S)
#     result = content.findall(pattern,content)
    result = getContentFromUrl(url, '<span style=.*?>(.*?)</span>')
    return result[0].decode('utf-8')[1]

def getContentFromUrl(url,pattern):
    response = urllib2.urlopen(url)
    content = response.read().decode('utf-8')
    patternS = re.compile(pattern,re.S)
    result = re.findall(patternS,content)
    return result


getPages(BlogListUrl)
getAllBlogs(BlogListUrl)
#getIContentFromUrl("http://www.court.gov.cn/cpwsw/sx/sxsyqszjrmfy/yxrmfy/ms/index_53.htm");
#getAllSegment()
