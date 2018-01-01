import urllib.request
from bs4 import BeautifulSoup
url = "http://www.douban.com/"

res = urllib.request.urlopen(url)
# 将res转成str
s0 = str(res)
# print(type(s0))
soup = BeautifulSoup(res, "html.parser")
# print(bs.prettify())
print(soup.title)

for link_tag in soup.find_all(''):
    print(link_tag.get(''))


# s = res.read()
#
# outfile = open('te.txt','wb')
# outfile.write(s)
# outfile.close()
