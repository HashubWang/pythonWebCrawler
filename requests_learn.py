import requests
from http import cookiejar
from bs4 import BeautifulSoup
import time
# 无法使用下面的代理，不知道为什么
# proxies ={
#     'http': 'socks5://45.78.48.215:1080',
#     'https':'socks5://45.78.48.215:1080',
# }
# response = requests.get("http://www.google.com")
# response1 = requests.get("http://www.youtube.com")
# response2 = requests.get("http://www.baidu.com")

# print(response2.content)

# print("Youtube status code: "+str(response1.status_code))
# print("Google status code: "+str(response.status_code))



