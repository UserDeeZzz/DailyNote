### 快速入门

#### 创建项目

```shell
django-admin startproject mysite # 创建项目
manage.py # 管理命令行工具
asgi.py # ASGI
wsgi.py # WSGI
settings.py # 配置文件
urls.py # 路由
```

#### 启动项目

```sh
ALLOWED_HOSTS = ['*'] # 在settings中设置允许所有ip请求
python manage.py runserver 0:8000
```

#### 创建应用

```sh
python manage.py startapp polls # 创建app
```

#### 配置路由

```python
# polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
]

# urls.py
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls'))
    #    path('admin/', admin.site.urls),
]
```

#### 配置app

```python
INSTALLED_APPS = [
    'django.contrib.auth',  # 认证授权
    'django.contrib.contenttypes',  # 内容类型
    'django.contrib.sessions',  # 会话
    'django.contrib.messages',  # 消息
    'django.contrib.staticfiles',  # 静态文件
    'polls.apps.PollsConfig',  # 自定义应用
]
```

#### 生成迁移数据

```sh
python manage.py makemigrations polls
```

#### 查看迁移sql

```sh
python manaeg.py sqlmigrate polls 0001
```

#### 迁移

```sh
python manage.py migrate
```

#### 启动交互式命令行

```sh
python manager.py shell
```

#### 启动数据库命令行

```
python manager.py dbshell
```

#### url命名空间

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

#### 视图

```python
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    # 获取对象获取不到返回404 官方提供的函数更简洁
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

#### 防跨站点请求伪造

```
{% csrf_token %} 
```

#### 通用视图

```python
from django.views import generic
path('', views.IndexView.as_view(), name='index')  # url配置
generic.ListView  # 继承类
generic.DetailView  # 继承类
```

#### 测试

```python
from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

```sh
python manage.py test polls
```

#### 测试视图

```python
python manage.py shell
from django.test.utils import setup_test_environment
setup_test_environment()


from django.urls import reverse
from django.test import Client

client = Client()
response = client.get(reverse('polls:index'))
response.status_code
```

### 模型

#### 字段选项

| 选项         | 用途                                                         |
| ------------ | ------------------------------------------------------------ |
| null         | 用于数据库，如果设置为 `True`，当该字段为空时，Django 会将数据库中该字段设置为 `NULL`。默认为 `False` |
| blank        | 用于表单验证，如果设置为 `True`，该字段允许为空。默认为 `False` |
| choices      | 每个二元组的第一个值会储存在数据库中，而第二个值将只会用于在表单中显示。 |
| default      | 该字段的默认值。可以是一个值或者是个可调用的对象，如果是个可调用对象，每次实例化模型时都会调用该对象 |
| help_text    | 额外的“帮助”文本，随表单控件一同显示。即便你的字段未用于表单，它对于生成文档也是很有用的。 |
| primary_key  | 如果设置为 `True` ，将该字段设置为该模型的主键               |
| unique       | 如果设置为 `True`，这个字段的值必须在整个表中保持唯一        |
| verbose_name | 如果未指定该参数值， Django 会自动使用字段的属性名作为该参数值，并且把下划线转换为空格,必要时 Djanog 会自动把首字母转换为大写。 |

#### 关联关系

##### 多对多

```
toppings = models.ManyToManyField(Topping)
```

##### 一对多

```
manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
```

##### 多对多添加额外属性

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
	# 查询group
    # ringo.membership_set.get(group__name='The Beatles')
    # ringo.membership_set.get(person__name='Ringo Starr')
    
    
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name
	# 查询members
    # beatles.members.all()
    # beatles.membership_set.get(person__name='Ringo Starr')
    # Group.objects.filter(members__name__startswith='Paul')
    
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    # Membership.objects.filter(person__name='Ringo Starr')
```

#### 元数据

```python
from django.db import models

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"
        abstract = True  # 抽象基类
```

#### 多标继承

```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    # 通过一个自动创建的 OneToOneField 
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```

#### 代理模型

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class OrderedPerson(Person):
    class Meta:
        ordering = ["last_name"]
        proxy = True
```

#### 创建对象

```python
b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()
```

#### 执行查询

Manager 是模型的 QuerySets 主要来源。每个模型至少有一个 Manager，默认名称是 objects,例如 Blog.objects.all() 返回了一个 QuerySet，后者包含了数据库中所有的 Blog 对象

`QuerySet` 是惰性的，只会在被 *计算* 时执行查询操作

```python
all() 返回数据表中所有对象
filter(**kwargs) 包含的对象满足给定查询参数
exclude(**kwargs) 包含的对象 不 满足给定查询参数
get() 检索单个对象 不包含或包含多个抛出异常
order_by('-headline') 排序
.all()[:5] 限制 QuerySet 条目数 OFFSET 5 LIMIT 5
```

#### F表达式

用于自己字段和字段比较计算

```python
from django.db.models import F
Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks') * 2)
```

#### Q表达式

完成复杂查询

你能通过 `&` 和 `|` 操作符和括号分组，组合任意复杂度的语句。当然， `Q` 对象也可通过 `~` 操作符反转，允许在组合查询中组合普通查询或反向 (`NOT`) 查询

```python
from django.db.models import Q
Q(question__startswith='Who') | Q(question__startswith='What')
Q(question__startswith='Who') & ~Q(pub_date__year=2005)
# 跟关键字参数一起 要放在最前面
Poll.objects.get(
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
    question__startswith='Who',
)
```

#### 一次修改多个对象

```
Entry.objects.filter(pub_date__year=2007).update(headline='Everything is the same')
```

#### 批量增加

```python
bulk_create()
```

#### 批量修改

```
bulk_update()
```

#### 批量插入

```
add()
```

#### 批量删除

```
remove()
```

#### 用sql语句查询

```python
Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
# 可以接受参数
Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
# 直接执行sql
from django.db import connection
```

#### 聚合

```python
# aggregate支持聚合操作 Sum Max Min Avg Count
# 对结果集所有条目汇总
from django.db.models import Sum, Max, Min, Avg, Count
Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))
# annotate 对每个条目进行聚合
Book.objects.annotate(Count('authors', distinct=True), Count('store', distinct=True))
# 每个书店价格区间
Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))
# 所有书店价格区间
Store.objects.aggregate(min_price=Min('books__price'), max_price=Max('books__price'))
# order_by() 排序
# values() 分组
```

#### 事务

```python
django中默认自动提交 # 设置项中AUTOCOMMIT=True
# 显式控制事务
from django.db import transaction
# 方式一
@transaction.atomic
def viewfunc(request):
    # This code executes inside a transaction.
    do_stuff()
 
# 方式二
def viewfunc(request):
    # This code executes in autocommit mode (Django's default).
    do_stuff()

    with transaction.atomic():
        # This code executes inside a transaction.
        do_more_stuff()
# 事务执行成功
@transaction.atomic
def viewfunc(request):

    a.save()
    # transaction now contains a.save()

    sid = transaction.savepoint()

    b.save()
    # transaction now contains a.save() and b.save()

    if want_to_keep_b:
        transaction.savepoint_commit(sid)
        # open transaction still contains a.save() and b.save()
    else:
        transaction.savepoint_rollback(sid)
        # open transaction now contains only a.save()

 with transaction.atomic():  # Outer atomic, start a new transaction
    transaction.on_commit(foo)

    try:
        with transaction.atomic():  # Inner atomic block, create a savepoint
            transaction.on_commit(bar)
            raise SomeError()  # Raising an exception - abort the savepoint
    except SomeError:
        pass

# foo() will be called, but not bar()
```

#### 多数据库设置

```python
# 根据app_label区分数据库 依次选择路由
DATABASES = {
    'default': {},
    'auth_db': {
        'NAME': 'auth_db',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_user',
        'PASSWORD': 'swordfish',
    },
    'primary': {
        'NAME': 'primary',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_user',
        'PASSWORD': 'spam',
    },
    'replica1': {
        'NAME': 'replica1',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_user',
        'PASSWORD': 'eggs',
    },
    'replica2': {
        'NAME': 'replica2',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_user',
        'PASSWORD': 'bacon',
    },
}
class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'auth', 'contenttypes'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'auth_db'
        return None
import random

class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        return random.choice(['replica1', 'replica2'])

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return 'primary'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_list = ('primary', 'replica1', 'replica2')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True
DATABASE_ROUTERS = ['path.to.AuthRouter', 'path.to.PrimaryReplicaRouter']

# 手动选择数据库
Author.objects.using('default').all()
my_object.save(using='legacy_users')
```

#### 自定义404

```python
# 最外面urls.py
handler404 = 'mysite.views.my_custom_page_not_found_view'
#404页面
@csrf_exempt  # 允许跨域
def page_not_found(request):
    return render_to_response('404.html')

```

#### 视图装饰器

```python
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass

require_GET # get
require_POST # post
require_safe  # get head
```

#### 文件上传

```
# 多文件上传
@require_http_methods(["GET", "POST"])
@csrf_exempt
def file(request):
    myfiles = request.FILES.getlist('myfile', None)
    for myfile in myfiles:
        path = os.path.join('.', myfile.name)
        with open(path, 'wb') as f:
            for chunk in myfile.chunks():
                f.write(chunk)
    return HttpResponse('upload success!')
```

#### 中间件

```python
# 中间件基类
MiddlewareMixin
# 视图之前 正序
process_request 
# 视图之前 正序
process_view
# 视图之后 倒序
process_response
# 视图执行后异常 倒序
process_exception
# 视图返回render template response 倒序
process_template_response
```

#### 会话

```python
在cookie里设置session_id=xxxxxx
在数据库redis缓存session信息 django-redis
中间件django.contrib.sessions为每个request对象添加session属性
# session_id 传到cookie
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 把这里缓存你的redis服务器ip和port
        "LOCATION": "redis://192.168.0.100:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# 我们定义一个cache(本地缓存来存储信息,cahe指定的是redis
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 指定本地的session使用的本地缓存名称是'default'
SESSION_CACHE_ALIAS = "default"
session结构 就是个redis里的hash
session_id:{
    "user_id":1,
	"company_id":2
}
# 调试session 
from django.contrib.sessions.backends.db import SessionStore
```

#### JWT

```
三部分
header {
    'alg': "HS256",
    'typ': "JWT"
}
payload
{
    "sub": '1234567890',
    "name": 'john',
    "admin":true
}
前两部分base64编码并用.拼接到一起加上secret
```

#### 文件处理api

```python
MEDIA_ROOT 
MEDIA_URL
with open('/path/to/hello.world', 'w') as f:
...     myfile = File(f)
...     myfile.write('Hello World')
from django.core.files.storage import FileSystemStorage
from django.db import models
# 内置文件存储类
fs = FileSystemStorage(location='/media/photos')

class Car(models.Model):
    ...
    photo = models.ImageField(storage=fs)
```

