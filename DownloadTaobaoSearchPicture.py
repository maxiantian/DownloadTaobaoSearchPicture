import urllib.request
import re
import ssl

#全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

#设置淘宝搜索的关键词
keyword = urllib.request.quote("毛衣")

#将爬虫伪装成火狐浏览器
headers=("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0")

#创建一个opener对象 
opener = urllib.request.build_opener()

#为opener设置header
opener.addheaders = [headers]

#将opener设为全局
urllib.request.install_opener(opener)

#为了方便测试，仅下载两页的数据
for i in range(0,2):

    #把关键词添加到URL中并请求数据
    url = "https://s.taobao.com/search?q="+ keyword +"&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180121&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s="+str(44*i)
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")

    #测试是否请求到数据
    print(len(data))

    #使用正则表达式进行匹配
    pat = '"pic_url":"//(.*?)"'
    imgs  = re.compile(pat).findall(data)

    for j in range(0,len(imgs)):

        #用匹配到的网址建立完整的URL，并直接下载到本地
        thisurl = "http://" + imgs[j]
        file = "/Users/Rocky1/Desktop/imgs/" + str(i) + "-" + str(j) + ".jpg"
        urllib.request.urlretrieve(thisurl,file)



 
    
