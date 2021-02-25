from django.db import models

# Create your models here.


"""
    千万不要在字段后面加  ，
    千万不要在字段后面加  ，
    千万不要在字段后面加  ，
    千万不要在字段后面加  ，
    千万不要在字段后面加  ，
    千万不要在字段后面加  ，
    千万不要在字段后面加  ，
    千万不要在字段后面加  ，
    
"""


# 用户账号信息
class User(models.Model):
    user = (
        ('1', '普通用户'),
        ('2', '会员'),
    )
    username = models.CharField(max_length=12, verbose_name='用户名')
    password = models.CharField(max_length=16, verbose_name='密码')
    is_vip = models.CharField(max_length=6, default='1', choices=user, verbose_name='是否是会员')

    class Meta:
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username


# 用户账号基本信息
class UserInfo(models.Model):
    addresses = (
        ('1', '安徽'),
        ('2', '湖南 '),
        ('3', '上海'),
        ('4', '北京')

    )
    genders = (
        ('1', '男'),
        ('2', '女'),
        ('3', '保密 ')
    )
    name = models.CharField(max_length=12, verbose_name='用户昵称')
    gender = models.CharField(max_length=5, choices=genders, verbose_name='性别')
    address = models.CharField(max_length=20, choices=addresses, verbose_name='用户地址')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    user = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='对应用户')
    header_pic = models.ImageField(upload_to='head_pic', verbose_name='头像', null=True, blank=True, default='head_pic/bird.jpg')

    class Meta:
        verbose_name_plural = '用户基本信息'

    def __str__(self):
        return self.name


# 用户类型账户
class VipUser(models.Model):
    user_type = (
        (1, '读者'),
        (2, '作者')
    )
    username = models.CharField(max_length=12, verbose_name='会员名')
    user_type = models.CharField(max_length=10,choices=user_type, verbose_name='小说类型')
    balance = models.IntegerField(default=0, verbose_name='余额')
    create_data = models.DateTimeField(verbose_name='会员创建时间')
    expires_data = models.DateTimeField(verbose_name='会员到期时间')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='对应用户')

    class Meta:
        verbose_name_plural = '会员信息'

    def __str__(self):
        return self.username


# 小说基本概述
class Books(models.Model):
    books_type = (
        (1, '玄幻修真'),
        (2, '仙侠武侠'),
        (3, '历史军事'),
        (4, '科幻游戏'),
        (5, '悬疑灵幻'),
        (6, '二次元'),
        (7, '免费'),
    )
    end = (
        (1, '未完结'),
        (2, '完结'),
    )
    # 书本信息
    book_name = models.CharField(max_length=30, verbose_name='书名')
    book_author = models.CharField(max_length=30, verbose_name='作者')
    book_num = models.IntegerField(primary_key=True, verbose_name='编号')
    book_info = models.TextField(verbose_name='小说简介')
    book_type = models.SmallIntegerField(choices=books_type, verbose_name='小说类型')
    book_hot = models.IntegerField(default=0, verbose_name='小说热度')
    book_end = models.SmallIntegerField(choices=end, verbose_name='是否完结')
    book_img = models.ImageField(upload_to='', verbose_name='小说图片', null=True, blank=True)

    def contr_text(self):
        if len(str(self.book_info)) > 80:  # 字数自己设置
            return '{}……'.format(str(self.book_info)[0:80])  # 超出部分以省略号代替。
        else:
            return str(self.book_info)

    class Meta:
        verbose_name_plural = '小说信息'

    def __str__(self):
        return self.book_name


# 小说章节
class BookChapter(models.Model):
    chapter_type = (
        (1, '免费'),
        (2, '会员'),
    )
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='chapter_book', verbose_name='小说名')
    chapters = models.CharField(max_length=30, verbose_name='小说章节')
    text = models.TextField(verbose_name='章节内容')
    chapter_types = models.CharField(max_length=5, choices=chapter_type)

    def contr_text(self):
        if len(str(self.text)) > 180:  # 字数自己设置
            return '{}……'.format(str(self.text)[0:180])  # 超出部分以省略号代替。
        else:
            return str(self.text)


    class Meta:
        verbose_name_plural = '小说章节信息'

    def __str__(self):
        return self.chapters


# 我的书架
class MyBooks(models.Model):
    books_type = (
        (1, '玄幻修真'),
        (2, '仙侠武侠'),
        (3, '历史军事'),
        (4, '科幻游戏'),
        (5, '悬疑灵幻'),
        (6, '二次元'),
        (7, '免费'),
    )
    book_master = models.CharField(max_length=10, null=True, blank=True)
    book_name = models.CharField(max_length=20, null=True, blank=True)
    book_num = models.BigIntegerField(primary_key=True)
    book_img = models.CharField(max_length=120, null=True, blank=True, verbose_name='小说图片')
    book_author = models.CharField(max_length=30, verbose_name='作者')
    book_type = models.SmallIntegerField(choices=books_type, verbose_name='小说类型')

    class Meta:
        verbose_name_plural = '我的书架'

    def __str__(self):
        return self.book_name


class Comment(models.Model):
    comment_master = models.CharField(max_length=20, verbose_name='评论用户')
    comment_text = models.TextField(verbose_name='评论内容')
    comment_data = models.DateTimeField(auto_now_add=True, verbose_name='评论日期')
    comment_book_name = models.CharField(max_length=50, verbose_name='评论对象')

    class Meta:
        verbose_name_plural = '用户评论'

    def __str__(self):
        return self.comment_master


