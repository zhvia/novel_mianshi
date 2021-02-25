# 冒泡
# def func(list):
#     length = len(list)
#     for i in range(0,length-1):
#         for j in range(0, length-1-i):
#             if list[j]>list[j+1]:
#                 list[j], list[j+1]=list[j+1], list[j]
#     print(list)
# i = [1,2,4,5,87,44,43,9,55,90,111,223,31,222,221,29,333]
# func(i)


# 选择
# def func(a):
#     lenth = len(a)
#     for i in range(lenth):
#         min_li = i
#         for j in range(i+1, lenth):
#             if a[min_li] > a[j]:
#                 min_li = j
#         a[i], a[min_li] = a[min_li],a[i]
#     print(a)
#
# i = [1,2,4,5,87,44,43,9,55,90,111,223,31,222,221,29,333]
# func(i)
# import re
#
# content = "asdasd1m123123,4255,asdsdfsdf,,,1ijio134ioj234jio234"
# rest = re.findall("\d+", content)
# print(rest)
# # 找出字符串中的字母
# rest = re.findall("[a-zA-Z]+", content)
# print(rest)


from selenium import webdriver
from time import sleep

# 创建浏览器驱动对象, 以为下创建不同浏览器驱动对象
# driver = webdriver.Chrome()    # Chrome浏览器

# driver = webdriver.Firefox()   # Firefox浏览器

# driver = webdriver.Edge()      # Edge浏览器

# driver = webdriver.Ie()        # Internet Explorer浏览器

# driver = webdriver.Opera()     # Opera浏览器

# driver = webdriver.PhantomJS()   # PhantomJS

# 打开指定网址
# driver.get('https://www.baidu.com')
# # 休眠3秒
# sleep(3)
# # 关闭浏览器驱动对象
# driver.quit()
