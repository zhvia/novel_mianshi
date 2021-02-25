import json
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from textApp.getToken import Token
from django.core.cache import cache
from django.utils.decorators import method_decorator
from textApp.form import MyForm
from textApp.models import *
# Create your views here.
from textApp import getCode
from textApp.models import User, UserInfo


# # 用户认证装饰器
def checklogin(func):
    def wrapper(request, *args, **kwargs):
        try:
            req_obj = json.loads(request.body)
            a = req_obj['token']
            if a:
                payload = Token.check_token(a)
                a = cache.get(payload['username'])
                if payload == 'token已失效' or payload == '非法的token' or payload == '非法的token':
                    return JsonResponse(payload, safe=False)
                else:
                    res = func(request, *args, **kwargs)
                    return res
            else:
                return JsonResponse('请登录', safe=False)
        except ValueError as e:
            print(e)
    return wrapper


# 用户登录的实现
def login(request):
    req_obj = json.loads(request.body)
    username = req_obj['username']
    password = req_obj['password']
    font_code = req_obj['code']
    back_code = request.session['value_code']
    try:
        user_obj = User.objects.filter(username=username)
        if user_obj:
            if User.objects.filter(username=username, password=password):
                if font_code.lower() == back_code.lower():
                    # 将用户登录成功的信息设置成token储存在redis里
                    redis_obj = Token.create_token(username, user_obj.first().is_vip)
                    # conn = get_redis_connection('default')
                    # conn.set(redis_obj, username, 15)
                    cache.set(username, redis_obj, 12*60*60)
                    obj = JsonResponse('suc', safe=False)
                    obj.set_cookie('token', redis_obj, 12*60*60)
                    return obj
                else:
                    return JsonResponse('验证码不正确', safe=False)
            else:
                return JsonResponse('密码不正确', safe=False)
        else:
            return JsonResponse('用户名不存在', safe=False)
    except Exception as e:
        print(e)
        return JsonResponse('fail', safe=False)


# 注册实现
def register(request):
    req_obj = json.loads(request.body)
    username = req_obj['username']
    password = req_obj['password']
    font_code = req_obj['code']

    back_code = request.session['value_code']
    if User.objects.filter(username=username):
        register_message = '用户名已存在'
        return JsonResponse(register_message, safe=False)
    else:
        if back_code.lower() == font_code.lower():
            user_obj = User.objects.create(username=username, password=password)
            user_obj.save()
            user = UserInfo.objects.create(
                user_id=user_obj.id,
                name=username,
                gender='3',
                address='1',
                phone='none',
            )
            user.save()
            return JsonResponse('suc', safe=False)
        else:
            return JsonResponse('验证码错误', safe=False)


# 注销实现
def logout(request):
    obj = JsonResponse('suc', safe=False)
    obj.delete_cookie('token')
    return obj


# 判断是否是vip
def vip(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'vip_user.html')


# 验证码图片的实现
def img(request):
    # 用 pillow 来制作验证码  并将验证码内容设置到cookie里
    data, code = getCode.get()
    request.session['value_code'] = code
    return HttpResponse(data, code)


# 首页显示所有图书
def index(request):
    books_objs = Books.objects.all()
    books_obj = serializers.serialize('json', books_objs)
    books = json.loads(books_obj)
    return JsonResponse(books, safe=False)


# def ajax_search(request):
#     if
#     info = request.POST.get('search_input')
#     print(info)
#     book = Books.objects.filter(book_name__contains=info)
#     b = serializers.serialize('json', book)
#     b = json.loads(b)
#     return HttpResponse(json.dumps(b))


# 搜索功能
def search(request):
    info = request.GET.get('bookinfo')
    # 检查输入框是否有值
    if info:
        # 按书名搜索
        books_name_obj = Books.objects.filter(book_name__contains=info)
        # 按作者搜索
        books_author_obj = Books.objects.filter(book_author__contains=info)
        book1 = serializers.serialize('json', books_name_obj)
        book2 = serializers.serialize('json', books_author_obj)
        book_name = json.loads(book1)
        book_author = json.loads(book2)
        data = {'book_name': book_name, 'book_author': book_author}
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse('请输入书名或作者', safe=False)


# 个人中心的实现
def my_zone(request):
    if request.method == 'POST':
        info = json.loads(request.body)['info']
        cookie = info['cookie']
        user = Token.check_token(cookie)['username']
        if user:
            name = info['username']
            phone = info['phone']
            gender = info['gender']
            address = info['address']
        # name = request.POST.get('name')
        # phone = request.POST.get('phone')
        # gender = request.POST.get('gender')
        # address = request.POST.get('address')
        # user = request.COOKIES.get('username')
            user_obj = User.objects.filter(username=user).first()
            user_upd = UserInfo.objects.filter(user_id=user_obj.id).update(
                name=name,
                phone=phone,
                address=address,
                gender=gender
            )
            return JsonResponse('suc', safe=False)
        else:
            return JsonResponse('fail', safe=False)
    else:
        cookie = request.GET.get('cookie')
        payload = Token.check_token(cookie)
        username = payload['username']
        # 一对一表单反向查询
        user_obj = User.objects.filter(username=username).first()
        name = user_obj.userinfo.name
        phone = user_obj.userinfo.phone
        # # 一对一表单正向查询
        # user_obj2 = UserInfo.objects.filter(name='那个男人').first()
        # print(user_obj2.user.username)
        # name = user_obj.userinfo.name
        gender = user_obj.userinfo.get_gender_display()
        address = user_obj.userinfo.get_address_display()
        # phone = user_obj.userinfo.phone
        data = {'name': name, 'phone': phone, 'address': address, 'gender': gender}
        return JsonResponse(data, safe=False)


# 我的书架功能实现
def my_books(request):
    token = request.GET.get('cookie')
    # 判断用户是否登陆
    if token:
        user = Token.check_token(token)
        username = user['username']
        my_books_obj = MyBooks.objects.filter(book_master=username)
        my_books_list = serializers.serialize('json', my_books_obj)
        my_books_json = json.loads(my_books_list)
        return JsonResponse(my_books_json, safe=False)
    else:
        return JsonResponse(None, safe=False)


# 将小说加入我的书架功能实现
def add_book(request):
    # 得到用户信息和小说的id
    cookie = request.GET.get('cookie')
    book_id = request.GET.get('book_id')
    # 如果用户登陆 则判断是否存在书架  若没有登陆则返回登陆
    if cookie:
        username = Token.check_token(cookie)['username']
        if book_id:
            if MyBooks.objects.filter(book_num=book_id, book_master=username):
                data = 'fail'
                return JsonResponse('不可重复添加 ', safe=False)
            else:
                book = Books.objects.filter(book_num=book_id).first()
                myBooks = MyBooks.objects.create(
                    book_name=book.book_name,
                    book_num=book_id,
                    book_master=username,
                    book_img=book.book_img,
                    book_author=book.book_author,
                    book_type=book.book_type
                    )
                myBooks.save()
                data = 'suc'
                return JsonResponse('添加成功', safe=False)
        else:
            state_code = 404
            return JsonResponse(state_code, safe=False)
    else:
        return JsonResponse('请登录', safe=False)


# 删除我的书架中的图书
def delete_mybook(request):
    # 找到用户选定的小说编号  并且循环找出单个书籍进行删除
    book_num_list_str = request.GET.get('book_num')
    book_num_list = json.loads(book_num_list_str)
    # 循环删除
    for book_num in book_num_list:
        print(book_num_list[book_num])
        MyBooks.objects.filter(book_num=book_num_list[book_num]).delete()
    return JsonResponse('suc', safe=False)


# 检查小说是否在我的书架  是则在前端显示已加入书架
def is_on_book(request):
    # 找到当前用户信息
    token = request.GET.get('cookie')
    username = Token.check_token(token)['username']
    # 找到小说的id 并且检查是否在我的书架中
    book_id = request.GET.get('book_id')
    is_true = MyBooks.objects.filter(book_num=book_id, book_master=username)
    if is_true:
        return JsonResponse('true', safe=False)
    else:
        return JsonResponse('false', safe=False)


# @login_type
def chapter(request):
    # 得到小说id
    book_id = request.GET.get('book_id')
    # 查询该小说
    book_obj = Books.objects.filter(book_num=book_id)
    # 将查到的小说章节按照id排序
    book_chapters_obj = BookChapter.objects.filter(books_id=book_id).order_by('id')
    # 序列化 并传到前端
    books = serializers.serialize('json', book_obj)
    book = json.loads(books)
    book_chapter = serializers.serialize('json', book_chapters_obj)
    book_chapters = json.loads(book_chapter)
    return JsonResponse({'book_chapter': book_chapters, 'book': book}, safe=False)


def chapter_info(request):
    chapter_id = request.GET.get('chapter_id')
    book_id = request.GET['book_id']
    cookie = request.COOKIES.get('token')
    play = Token.check_token(cookie)
    # 找到书信息  和 章节的信息
    book_type = Books.objects.filter(book_num=book_id).first().book_type
    chapter_infos = BookChapter.objects.filter(books_id=book_id, id=chapter_id).first()
    # 如果书是免费的 返回全部章节信息
    if book_type == '7':
        chapters = chapter_infos.chapters
        text = chapter_infos.text
        message = 'ok'
        book_chapter = {'chapter': chapters, 'text': text, "message": message}
        return JsonResponse(book_chapter, safe=False)
    # 如果不是免费的 则判断用户类型
    else:
        if chapter_infos.chapter_types == '1':
            chapters = chapter_infos.chapters
            text = chapter_infos.text
            message = 'ok'
            book_chapter = {'chapter': chapters, 'text': text, "message": message}
            return JsonResponse(book_chapter, safe=False)
        else:
            token = request.COOKIES.get('token')
            # 如果用户登录过
            if token:
                play = Token.check_token(token)
                username = play['username']
                is_vip = play['is_vip']
                user = User.objects.filter(username=username)
                # 判断用户类型 如果是会员 返回全部章节信息
                if user and user.first().is_vip == '2' and is_vip == '2':
                    chapters = chapter_infos.chapters
                    text = chapter_infos.text
                    message = 'ok'
                    book_chapter = {'chapter': chapters, 'text': text, "message": message}
                    return JsonResponse(book_chapter, safe=False)
                # 否则返回部分信息
                else:

                    chapters = chapter_infos.chapters
                    text = chapter_infos.contr_text()
                    print(chapters)
                    message = '亲！您还不是会员哟'
                    book_chapter = {'chapter': chapters, 'text': text, "message": message}
                    return JsonResponse(book_chapter, safe=False)
        # 如果没登陆也返回部分信息
            else:
                chapters = chapter_infos.chapters
                text = chapter_infos.contr_text()
                message = '亲,您还没有登录不能阅读哦'
                book_chapter = {'chapter': chapters, 'text': text, "message": message}
                return JsonResponse(book_chapter, safe=False)


# from textApp import webCrawler
#
# from urllib import request as request_de
# import pymysql
#
# import requests as requests_de
# from lxml import etree
# import re
# import time
# from bs4 import BeautifulSoup
#
# def python_bug(request):
#     src = 'https://www.bqkan.com'
#     name = ''
#     author = ''
#     text = ''
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
#     }
#     url = 'https://www.bqkan.com/83641_83641553/'
#     res = requests_de.get(url, headers=headers)
#     res.encoding = res.apparent_encoding
#     soup = BeautifulSoup(res.text, 'html.parser')
#     names = soup.select('body > div.book > div.info > h2')
#     authors = soup.select('body > div.book > div.info > div.small > span:nth-child(1)')
#     texts = soup.select('body > div.book > div.info > div.intro')
#     select = etree.HTML(res.text)
#     imgs = select.xpath('//div[@class="cover"]//img/@src')
#     for m in imgs:
#         src += str(m)
#     for i in names:
#         name += str(i)
#     for l in authors:
#         author += str(l)
#     for x in texts:
#         text += str(x)
#     patter = re.compile('<(.*?)>')
#     name = patter.sub('', name)
#     author = patter.sub('', author)
#     text = patter.sub('', text)
#     print(src)
#     # for i in range(1):
#     request_de.urlretrieve(src, '../static/book_images/{}.jpg'.format("2"))
#     book = Books.objects.create(
#             book_name=name,
#             book_author=author,
#             book_num=5,
#             book_info=text,
#             book_type='1',
#             book_end='1',
#             book_hot=0,
#             book_img='{}.jpg'.format(i))
#     return HttpResponse('ok')


def chapter_normal(request, book_id):
    book = Books.objects.filter(book_num=book_id).first()
    book_chapters = BookChapter.objects.filter(books_id=book_id)
    return render(request, 'chapter_normal.html', locals())


