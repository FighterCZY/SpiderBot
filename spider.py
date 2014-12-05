#encoding=utf8
import requests
from bs4 import BeautifulSoup
###登录页的url
url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'
###有些网站反爬虫，这里用headers把程序伪装成浏览器
header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36' }
###登录需要提交的表单

max = 0
OUR = 83779
for i in range(OUR):
    a = 'EAC15900'
    temp = "%05d" % (OUR-i)
    b = a + temp
    form_data = { 'changeLocale':'',
        'appReceiptNum':b, #填入网站的上网帐号
        'initCaseSearch':'CHECK STATUS',  #填入网站密码（加密后的）
    }
    s = requests.session()
    response = s.post(url,data = form_data,headers = header)
    html = response.text
    soup = BeautifulSoup(html)
    ss = str(soup.p)
    head = str(soup.h1)
    if ss.find("I-765") != -1 and head.find("Approved") != -1:
        max = OUR-i
        break  

print max