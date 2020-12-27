# fillunivircitylist.py
import requests
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, headers={'user-agent': 'Mozilla/5.0'}, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取失败')
        return ''

def fillUnivList(html):
    ulist = []
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            ulist.append([tds[0].text.strip(), tds[1].text.strip(), tds[4].text.strip()])
    return ulist

def printUnibList(ulist, num):
    tmpl = '{0:^5}{1:{3}^20}{2:^5}'
    print(tmpl.format('排名', '大学名称', '分数', chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tmpl.format(u[0], u[1], u[2], chr(12288)))

def main():
    url = 'https://www.shanghairanking.cn/rankings/bcur/202011'
    html = getHTMLText(url)
    ufo = fillUnivList(html)
    printUnibList(ufo, 50)

main()
