import requests
import httpie
from pprint import pprint

url = "https://book.douban.com/tag/%E6%94%BF%E6%B2%BB"  # url encode, (must be ascii)

httpie

# python -m httpie -p HBh url,  allows us to check the headers.

r = requests.get(url)
r.status_code  # 418, 反爬虫
pprint(dict(r.headers))

# 解决方法: bottom up or top down:
# 先拿到 cURL command, with all headers info
# 用最复杂的能过的浏览器header, 然后一步步删减到mvp;
# Or 用最简单的空header 一条条增加到mvp

# it should look like this:
# curl 'https://book.douban.com/tag/%E6%94%BF%E6%B2%BB' \
#   -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
#   -H 'Accept-Language: en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7' \
#   -H 'Cache-Control: max-age=0' \
#   -H 'Connection: keep-alive' \
#   -H 'Cookie: ll="108231"; bid=S1MNfiGEOMw; __utmc=30149280; __utmz=30149280.1689396254.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _vwo_uuid_v2=D5C3D2E540BB7C0513A5C4D10FF579DB8|2a620158143ea6ecdb6f430d048e98ee; __utmc=81379588; __utmz=81379588.1689396286.1.1.utmcsr=movie.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/chart; _pk_id.100001.3ac3=b4c1110bdbfbdd09.1689396295.; __utma=30149280.1067863067.1689396254.1689396254.1689410113.2; __utmt_douban=1; __utmb=30149280.1.10.1689410113; __utma=81379588.1016777538.1689396286.1689396286.1689410113.2; __utmt=1; __utmb=81379588.1.10.1689410113; _pk_ses.100001.3ac3=1; ap_v=0,6.0' \
#   -H 'Referer: https://book.douban.com/tag/%E5%8E%86%E5%8F%B2' \
#   -H 'Sec-Fetch-Dest: document' \
#   -H 'Sec-Fetch-Mode: navigate' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'Sec-Fetch-User: ?1' \
#   -H 'Upgrade-Insecure-Requests: 1' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   --compressed
# NOTE HERE the H is for header, just like in httpie
# directly execute this curl in console could give you return you the page
# google what is cURL?

# then convert this cURL command into python (using some online tool, just google)
# e.g. https://curlconverter.com/

# then you get the python request


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://book.douban.com/tag/%E5%8E%86%E5%8F%B2',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}  # most important three: user agent, referer, accept

import requests
from lxml import etree

response = requests.get('https://book.douban.com/tag/%E6%94%BF%E6%B2%BB', headers=headers)
response.status_code  # 200
html_text = response.text

page = etree.HTML(html_text)
title_xpath = r"//div[2]/h2[1]/a[1]"
titles = page.xpath(title_xpath)
print([e.text.strip() for e in titles])

pprint([e.text for e in titles])  # 再用regex把文字提取出来就行了
pprint([e.text.strip() for e in titles])

# 也可以直接用更高级一点的xpath语法, 在最后一个element后加上 text(), 直接提取text
title_xpath_2 = r"//div[2]/h2[1]/a[1]/text()"
title_texts = page.xpath(title_xpath_2)
print(title_texts)
