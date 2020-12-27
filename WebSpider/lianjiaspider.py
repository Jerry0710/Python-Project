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
    re_area = re.compile(r'\d*室\d*厅.*平米')
    # div = soup.find('div', class_='item')
    for li in soup.find_all('li', class_="clear LOGVIEWDATA LOGCLICKDATA"):
        location = li.find('div', class_="flood").text.strip()
        area = re_area.search(li.find('div', class_="address").text).group(0)
        price = li.find('div', class_="totalPrice").text.strip()
        ilt.append([location, area, price])
        print('\r爬虫进度：{}'.format(len(ilt)), end='')


def print_goods_list(ilt):
    tplt = '{:^4}\t{:^8}\t{:<16}'
    print(tplt.format('序号', '价格', '商品名称'))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))

def write_goods_list(ilt, path):
    tplt = '{0:^4}\t{1:{4}^30}\t{2:{4}^15}\t{3:^8}'
    count = 0
    with open(path, 'a+t') as f:
        f.write(tplt.format('序号', '楼盘名称', '房型', '价格', chr(12288)) + '\n')
        for g in ilt:
            count += 1
            f.write(tplt.format(count, g[0], g[1], g[2], chr(12288)) + '\n')

if __name__ == '__main__':
    ilt = []
    location = '南沙'
    depth = 3
    for i in range(depth):
        url = 'https://gz.lianjia.com/ershoufang/nansha/pg{}rs{}/'.format((i + 1) * 2 - 1, location)
        html = get_html_text(url)
        parse_page(ilt, html)
    path = '/Users/zoe/PycharmProjects/netspider/user/ulist.txt'
    write_goods_list(ilt, path)
