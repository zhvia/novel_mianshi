from selenium import webdriver
from urllib import request
from lxml import etree

web = webdriver.Chrome('https://i.qq.com/')
web_text = web.page_source

