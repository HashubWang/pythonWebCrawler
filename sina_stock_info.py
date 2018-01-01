import requests

num = input("请输入个股的股票代码： ")

socket_response=requests.get("http://hq.sinajs.cn/list=sz"+num)
str = socket_response.content
decode_str=str.decode('gbk')

result = decode_str.replace('var hq_str_sz'+num+'="', '').replace('";\n', '').split(',')
header = [
'股票名：'
,'今日开盘价：'
,'昨日收盘价：'
,'当前价格：'
,'今日最高价：'
,'今日最低价:'
,'竞买价，即“买一“报价；'
,'竞卖价，即“卖一“报价；'
,'成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百：'
,'成交金额，单位为“元“，为了一目了然，通常以“万元“为成交金额的单位，所以通常把该值除以一万：'
,'买一”申报股数'
,'买一”报价：'
,'买二”申报股数：'
,'买二”报价 '
,'买三”申报股数 '
,'买三”报价 '
,'买四”申报股数 '
,'买四”报价 '
,'买五”申报股数 '
,'买五”报价 '
,'卖一”申报股数 '
,'卖一”报价 '
,'卖二申报股数 '
,'卖二报价 '
,'卖三申报股数 '
,'卖三报价 '
,'卖四申报股数 '
,'卖四报价 '
,'卖五申报股数：'
,'卖五报价：'
,'日期：'
,'时间：'
,'无视此项！！']

for (header,result) in zip(header, result):
    final = header+result
    print(final)