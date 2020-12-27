import requests
import re
import bs4


def get_html_text(url):
    try:
        r = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parse_page(ilt, html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    div = soup.find('div', id="J_goodsList")
    for li in div.find_all('li', class_="gl-item"):
        price = li.find('div', class_="p-price").text.strip().replace('\n', ' ')
        description = li.find('div', class_="p-name p-name-type-2").text.strip().replace('\n', ' ')
        ilt.append([price, description])
        print('\r爬虫进度：{}'.format(len(ilt)), end='')


def print_goods_list(ilt):
    tplt = '{:^4}\t{:^8}\t{:<16}'
    print(tplt.format('序号', '价格', '商品名称'))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))

def write_goods_list(ilt, path):
    tplt = '{:^4}\t{:^8}\t{:<16}'
    count = 0
    with open(path, 'a+t') as f:
        f.write(tplt.format('序号', '价格', '商品名称'))
        for g in ilt:
            count += 1
            f.write(tplt.format(count, g[0], g[1]) + '\n')

if __name__ == '__main__':
    ilt = []
    goods = '电钻'
    depth = 2
    url = 'https://search.jd.com/Search?keyword=' + goods
    for i in range(depth):
        uri = url + '&page={}'.format((i + 1) * 2 - 1)
        html = get_html_text(uri)
        parse_page(ilt, html)
    path = '/Users/zoe/PycharmProjects/netspider/user/ulist.xlsx'
    write_goods_list(ilt, path)
    # print_goods_list(ilt)
