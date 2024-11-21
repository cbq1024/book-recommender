"""
推荐数据集和相关实用程序
"""

import re
import requests
import csv

def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    items = parse_result(html)  # 解析 过滤我们想要的信息

    # 打开 CSV 文件并准备写入
    with open('../data/dang2-book.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['排名', '图书封面', '图书名', '图书评论数', '五星评分', '作者', '出版社', '五星评分次数', '图书折后价', '图书原价', '折扣额度']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 如果是第一页，写入标题行
        if page == 1:
            writer.writeheader()

        # 写入每一行数据
        for item in items:
            print(item)  # 打印测试获取到的信息
            writer.writerow(item)  # 写入获取到的信息到CSV

# 获取源代码
def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def parse_result(html):
    '''
    :param html:
    :return:
    下标0:图书排名
    下标1：图书封面
    下标2：图书名
    下标3：图书评论数
    下标4：五星评分
    下标5：作者名称
    下标6：出版社
    下标7：五星评分次数
    下标8：图书折后价
    下标9：图书原价 <span\sclass="price_r">&yen;(.*?)</span>.*?
    下标10：折扣额度 <span\sclass="price_s">(.*?)</span>.*?
    '''
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?target="_blank">(.*?)</a>.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?<span\sclass="price_r">&yen;(.*?)</span>.*?<span\sclass="price_s">(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '排名': item[0],
            '图书封面': item[1],
            '图书名': item[2],
            '图书评论数': item[3],
            '五星评分': item[4],
            '作者': item[5],
            '出版社': item[6],
            '五星评分次数': item[7],
            '图书折后价': item[8],
            '图书原价': item[9],
            '折扣额度': item[10]
        }

if __name__ == '__main__':
    # 自动获取25页500条数据
    for i in range(1, 26):
        main(i)
