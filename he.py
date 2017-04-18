import re
import urllib.request
import urllib

def downloadPage(url):
    try:
    	h = urllib.request.urlopen(url)
    except:
    	print(1)	
    return h.read().decode('utf-8').replace(u'\xa9', "u")

def downloadImg(content):
    pattern = r'src="(.+?\.jpeg)"'
    m = re.compile(pattern)
    urls = re.findall(m, content)
    print(urls)

    for i, url in enumerate(urls):
        print (url)
        urllib.request.urlretrieve(url, "%s.jpeg" % (i, ))

try:
	content = downloadPage("https://www.duitang.com/search/?kw=%E7%81%AB%E5%BD%B1&type=feed")
except:
	print(111)
downloadImg(content)