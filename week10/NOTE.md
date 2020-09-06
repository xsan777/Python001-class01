学习笔记

毕业项目：构建一个舆情分析平台

项目背景：某公司计划新上线一款苏打水饮料，为了了解用户对苏打水的接受程度，需要抓取“什么值得买”( https://www.smzdm.com/fenlei/qipaoshui/ ) 网站中气泡水种类前 10 的产品的用户评论，通过对用户评论的正向、负向评价了解排名前 10 的气泡水产品的用户接受程度。

注意：
由于这个网站的产品是实时更新的，一些新的气泡水产品可能没有足够数量的评论，大家可以将气泡水替换为其他产品，比如：

    手机产品 24 小时排行 https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/
    电脑游戏最新排行 https://www.smzdm.com/fenlei/diannaoyouxi/
    洗发护发产品 24 小时排行 https://www.smzdm.com/fenlei/xifahufa/h5c4s0f0t0p1/#feed-main/

具体需求：

    正确使用 Scrapy 框架或 Selenium 获取评论，如果评论有多页，需实现自动翻页功能，将原始评论结果存入 MySQL 数据库，并使用定时任务每天定期更新。
    对评论数据进行清洗（可借助 Pandas 库），并进行语义情感分析，将分析结果存入数据库。
    使用 Django 集成在线图表对采集数、舆情进行展示，需包括该产品正、负评价比例，以及评价内容等。
    数据展示支持按时间筛选和按关键词筛选功能（参考百度情感分析后台 https://ai.baidu.com/tech/nlp_apply/sentiment_classify）。

评分标准：（实现相应功能，每项 +10 分，部分实现 +5 分）

    正确使用 Scrapy 框架获取评论，如果评论有多页，需实现自动翻页功能。
    评论内容能够正确存储到 MySQL 数据库中，不因表结构不合理出现数据截断情况。
    数据清洗后，再次存储的数据不应出现缺失值。
    Django 能够正确运行，并展示采集到的数据，数据不应该有乱码、缺失等问题。
    在 Django 上采用图表方式展示数据分类情况。
    舆情分析的结果存入到 MySQL 数据库中。
    在 Django 上采用图表方式展示舆情分析的结果。
    可以在 Web 界面根据关键字或关键词进行搜索，并能够在页面展示正确的搜索结果。
    支持按照时间（录入时间或评论时间）进行搜索，并能够在页面展示正确的搜索结果。
    符合 PEP8 代码规范，函数、模块之间的调用高内聚低耦合，具有良好的扩展性和可读性。


# 作业完成过程

## 爬取数据放入数据库

### 创建scrapy爬虫
```shell
    scrapy -help
    scrapy startproject qipaoshui
    scrapy genspider smzdm smzdm.com/fenlei/qipaoshui
    scrapy startproject shouji
    scrapy genspider smzdm smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/
```

## 爬取数据放入数据库

### 创建scrapy爬虫
```shell
    scrapy -help
    scrapy startproject qipaoshui
    scrapy genspider smzdm www.smzdm.com/fenlei/qipaoshui
```
### 获取评论
```python
    for i in range(0,30):
            print('='*50)
            for j in range(0,len(self.max_collect)):
                if int(collects[i]) > int(self.max_collect[j]):
                    self.max_link.insert(j,links[i])
                    self.max_collect.insert(j,collects[i])
        
        for i in range(0,10):
            print('~'*50)
            item['collect'] = self.max_collect[i]
            yield scrapy.Request(url = self.max_link[i], meta = {'item': item}, callback = self.parse2,dont_filter = True)

```
### 运行爬虫获取数据
```shell
    scrapy crawl smzdm
```
## 创建Django项目

##  创建管理员账户

- 创建Django管理员用户
  ```Shell
  python manage.py createsuperuser
  ```
  admin admin@admin.com 123456

### 创建 Django 项目 
    *django-admin startproject MyDjango

### 创建 Django 应用程序 
     
    * python manage.py startapp qipaoshui
    * setting.py 添加app 添加数据库设置 
    * urls调度器 增加项目urls 增加index的urls

    * python manage.py makemigrations 
    * python manage.py migrate

### pip install snownlp

    *python manage.py runserver
    *python manage.py inspectdb

### pip install apscheduler 定时任务框架


### 用到的路径资源
```text
然后打开postman软件  官网是https://www.postman.com/


这种不是表情符，是 html 字符实体
https://www.w3school.com.cn/html/html_entities.asp
就不算乱码了，如果想处理的话可以替换掉，也可以用 django 的 {% autoescape off %}{% endautoescape %} 标签处理


scrapy框架异常之no more duplicates will be shown (see DUPEFILTER_DEBUG to show all duplicates)
https://blog.csdn.net/qq_40176258/article/details/86527568

https://markdown-zh.readthedocs.io/en/latest/ 来快速学习一下markdown的基本语法哈

为使用了 multiprocessing  的程序，提供冻结以产生 Windows 可执行文件的支持
https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#multiprocessing.freeze_support


从零搭建Redis-Scrapy分布式爬虫
https://www.cnblogs.com/alexzhang92/p/9410339.html


vscode pylint报错的问题
https://www.jianshu.com/p/5184ae0b0fc6



今天的第二波干货分享，助教老师肖伟翼关于Python代码规范的几条说明（助教老师佳兴对第2、8条做了一些细节补充）。

Python常用规范或习惯，代码写给人看的，为了自己和同事将来维护方便，应遵照规范和习惯编写：

1.变量名和方法用小写和下划线命名，类名用首字母大写驼峰命名。
2.每个import独占一行，import尽量放在文件顶部，可以分为三部分，先import标准库，再import第三方库，最后才是程序的其他模块。每部分以一个空行做间隔。
3.每行代码不宜过长，过长时应适当换行，换行不建议用反斜杠连接，建议用圆括号括起语句换行。
4.导入语句、函数、类之间要适当隔行。
5.程序入口应放在if __name__ == '__main__'下。
6.每个函数或方法代码行数不宜过多，过多时应考虑是否可拆分功能。
7.建议避免if或者for的过多层嵌套，适当用break、continue、return等减少嵌套层数。
8.遵照IDE的提示，把不规范的代码改掉。每个IDE都有格式化快捷键，PyCharm Windows 下默认为Ctrl+Alt+L(mac 下为 command+option+L)，VSCode Windows 下默认为Shift+Alt+F(mac 下为 shift+option+F)，建议与Ctrl+S保存一样多使用。



第三周的作业，助教老师樊星也给出了自己的代码示例，同学们可以参考学习：https://github.com/star-fx/Python001-class01/blob/master/week03/pmap.py

1，scrapy获取快代理中的代理ip 2，scrapy获取89代理的代理ip
https://gitee.com/jianchao_w/agent_ip/blob/master/proxySpider/proxySpider/spiders/proxy.py

Paste from 数据横向存
https://paste.ubuntu.com/p/J8xPgrwYsN/

pycharm 有些库（函数）没有代码提示
https://blog.csdn.net/nima1994/article/details/70344682

知乎，如何入门python爬虫
https://www.zhihu.com/question/20899988/answer/783269460

Yield 和 return的区别
https://www.jianshu.com/p/a3383b144eb6

你可以执行类似 python3.7 -m pip xxx 这种方式是下，看看调用的是不是 3.7 版本的

scrapy Architecture overview
https://docs.scrapy.org/en/latest/topics/architecture.html

python利用os.system执行多条系统命令
https://my.oschina.net/u/3636678/blog/2986082

https://docs.python.org/zh-cn/3/library/os.html#os.system


看完这几周的作业，助教老师樊星有三点小建议想分享给同学们：

1. 分解任务。要多思考如何合理分解任务到多个方法，或多个类的多个方法，而不是全部写到一起。
2. 多线程/多进程问题。Python 提供了对于多线程/多进程操作的底层和高阶抽象，底层抽象大概包括 threading 和 multiprocessing 这 2 个包里的类和方法，高阶抽象大概包括了 concurrent.futures 包里的类和方法，大家在使用时要注意区分，如果把2种抽象中的 API 混合使用，逻辑就会比较乱，要尽量避免。
3. 读官方文档，读官方文档，读官方文档，重要的文档读3遍。例1：有同学使用 os.system 来调用系统的 ping 命令，但是去看下 os.system 的文档，里面写了 Python 官方建议使用 subprocess 库中的方法来代替 os.system 方法。例2：有同学自己实现了计算 2 个 IP 之间所有 IP 的功能（学会自己实现这个共功能当然是好事儿），其实只要去看看 ipaddress 库的文档，就会发现它已经提供了 ipaddress.summarize_address_range 这个方法来满足需求。



```


常见报错
1.  django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'
    解决方法：在 __init__.py 文件中添加以下代码即可
    import pymysql
    pymysql.install_as_MySQLdb()

2.   version = Database.version_info
    # if version < (1, 3, 13):
    # raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

3.  AttributeError: 'str' object has no attribute 'decode'
    出现这个错误之后可以根据错误提示找到文件位置，打开 operations.py 文件，找到以下代码：
    def last_executed_query(self, cursor, sql, params):
    query = getattr(cursor, '_executed', None)
    # if query is not None:
    #     query = query.decode(errors='replace')
    return query





django 数据库设置：

```python
    
result = self._query(query)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class QipaoshuiQipaoshui(models.Model):
    collect = models.IntegerField()
    estimate = models.TextField()
    sentiment = models.FloatField()

    class Meta:
        managed = False
```