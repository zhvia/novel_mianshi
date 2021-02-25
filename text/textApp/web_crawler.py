import time
from urllib import request

import pymysql
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ChromeOptions
# 设置chrom的值  可爬


def book_info(url2, id):
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    bro = webdriver.Chrome(options=option)
    # 让浏览器对指定url发起访问
    bro.get(url2)
    # 获取浏览器当前打开页面的页面源码数据(可见即可得)
    page_text = bro.page_source
    time.sleep(1)
    tree = etree.HTML(page_text)
    src = 'https://www.bqkan.com/'
    name = tree.xpath('/html/body/div[4]/div[2]/h2/text()')[0]
    author = tree.xpath('/html/body/div[4]/div[2]/div[2]/span[1]/text()')[0]
    info = tree.xpath('/html/body/div[4]/div[2]/div[3]/text()[1]')[0]
    img_src = tree.xpath('/html/body/div[4]/div[2]/div[1]/img/@src')[0]
    src = src + str(img_src)
    img = request.urlretrieve(src, '../static/book_images/{}.jpg'.format(name))
    name1 = str(name)
    author1 = str(author)
    info1 = str(info)
    src_img = name+'.jpg'

    con = pymysql.connect(
        # host='121.196.99.25',
        # user='zhengwei',
        # password='Zw970306.',
        # database='web'
        host='localhost',
        user='root',
        password='root',
        database='web'
    )
    cur = con.cursor()

    sql = "insert into textApp_books (book_name, book_author, book_num, book_info, book_hot, book_type, book_end, book_img)" \
          " values('%s', '%s', %d, '%s', %d, %d, %d, '%s');"%(name1,author1,id,info1,1,1,1,src_img)

    cur.execute(sql)
    con.commit()
    con.close()
    print('###成功')
    time.sleep(1)
    bro.quit()


def book_chapter(url2, id):
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    bro = webdriver.Chrome(options=option)
    # 让浏览器对指定url发起访问
    bro.get(url2)
    # 获取浏览器当前打开页面的页面源码数据(可见即可得)

    page_text = bro.page_source
    time.sleep(1)
    tree = etree.HTML(page_text)
    for i in range(13, 103):
        a_text = '/html/body/div[5]/dl/dd[{}]/a/text()'.format(i)
        chapters = tree.xpath(a_text)[0]
        chapters1 = str(chapters)
        print(chapters1)
        a_src = '/html/body/div[5]/dl/dd[{}]/a/@href'.format(i)
        src = tree.xpath(a_src)[0]
        src_all = 'https://www.bqkan.com/'+src

        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        web = webdriver.Chrome(options=option)
        # 让浏览器对指定url发起访问
        web.get(src_all)
        # 获取浏览器当前打开页面的页面源码数据(可见即可得)
        page_text = web.page_source
        select = etree.HTML(page_text)
        text = select.xpath('//*[@id="content"]/text()')
        text1 = ''.join(text)
        print(type(text1))
        time.sleep(1)
        con = pymysql.connect(
            # host='121.196.99.25',
            # user='zhengwei',
            # password='Zw970306.',
            # database='web'
            host='localhost',
            user='root',
            password='root',
            database='web'
        )
        cur = con.cursor()

        sql = "insert into textApp_bookchapter (chapters, text, books_id) value ('%s', '%s', '%s')"%(chapters1, text1, id)

        cur.execute(sql)
        con.commit()
        con.close()
        print('###成功')
        time.sleep(1)
        bro.quit()
        web.quit()


if __name__ == '__main__':
    url2 = ['https://www.bqkan.com/0_{}/'.format(str(i)) for i in range(1, 100)]
    id = 1
    for url in url2:
        book_info(url, id)
        book_chapter(url, id)
        id += 1





