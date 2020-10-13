# round用法
# 求round(16732,-1)
print(round(16732, -1) == 16730)
# 集合无序 List有序

# 引用外部变量
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10) == 30 and b(10) == 30)

# namedtuple

from collections import namedtuple

Employee = namedtuple('Employee', ('name', 'age'))
e = Employee(*('deez', 18))
print(e.name == 'deez')
print(e.age == 18)


# redis数据类型
# zset set str list hash Hyperloglog bitmap

# 迭代器协议

class Node:
    def __init__(self, val):
        self._children = []
        self.val = val
        self._iterator = None

    def __iter__(self):
        # 可迭代对象
        print("iter......")
        return self

    def __next__(self):
        """迭代器"""
        print('next...')
        if self._iterator is None:
            self._iterator = iter(self._children)
        return next(self._iterator)

    def add_child(self, val):
        self._children.append(val)


node = Node(10)
for i in range(10):
    node.add_child(i)

for i in node:
    print(i)

# 生成器
import os


def walk(d):
    for fn in os.listdir(d):
        np = os.path.join(d, fn)
        if os.path.isdir(np):
            for k in walk(np):
                yield k
        else:
            yield np


# 字典根据value排序
d = {
    'a': 30.1,
    'b': 50.1,
    'c': 40.1,
    'd': 20.1,
}
l = sorted([(v, k) for k, v in d.items()])
print((l[0], l[-1]))

# 上下文管理器
# import socket
#
#
# class Connection:
#
#     def __init__(self, addr, port):
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.addr = addr
#         self.port = port
#
#     def __enter__(self):
#         print()
#         self.sock.connect((self.addr, self.port))
#         return self.sock
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.sock.close()


# with Connection('127.0.0.1', 8000) as c:
#     while true:
#         data = c.recv(1024).decode('utf8')
#         if data == 'quit':
#             true = False
#         print('recevie news:\033[5;37;46m%s\033[0m' % data)

# 多线程
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=5) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())


# 单例模式

class SingleTon:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            setattr(cls, '_instance', object.__new__(cls))
        return getattr(cls, '_instance')


# gc
# 引用计数 创建对象 引用对象都会将计数+1 删除引用或删除对象-1
# 分代回收 是代表0 1 2 在第0代对象数量达到700个之前，不把未被回收的对象放入第一代；而在第一代对象数量达到10个之前也不把未被回收的对象移到第二代
# 标记清除 解决循环引用 引用关系有向图 从gc root object遍历有向图达到的点被标记 没被标记的被清除
import time


# 装饰器
def clock(timeout):
    def outer(func):
        def inner(*args, **kwargs):
            s = time.perf_counter()
            func(*args, **kwargs)
            e = time.perf_counter()
            if e - s > timeout:
                print("超时")
            else:
                print(e - s)

        return inner

    return outer


@clock(1)
def t(a, b):
    return pow(a, b)


t(25, 13)


# 属性描述符 将一个类的属性设置托管
class Descriptor:

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        print("设置属性")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print("获取属性", instance, owner)
        return instance.__dict__.get(self.name, None)

    def __delete__(self, instance):
        print("删除属性")
        if self.name in instance.__dict__:
            instance.__dict__.pop(self.name)


class T:
    pass


# 获取属性的钩子函数
class Person(T):
    age = Descriptor('age')

    def __getattribute__(self, item):
        print("获取属性先经过这")
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("属性不存在才调到这")
        return super().__getattr__(item)

    def __setattr__(self, key, value):
        print("设置属性才调到这")
        super(Person, self).__setattr__(key, value)

    def __delattr__(self, item):
        print("删除属性才调到这")
        super().__delattr__(item)


p = Person()
p.age = 20
p.name = 'deez'
print(p.age)
print(p.hha)

# 列表生成
s = [i for i in range(5) if i % 2 == 0]
s = [i if i % 2 == 0 else i ** 2 for i in range(5)]


# 元类
# 类创建实例 而元类创建类
# type关键字创建类
# Example = type('Example',(继承父类,),attrs) 动态创建类

class ExampleMeta(type):
    def __new__(mcs, kls, bases, attrs):
        # 所有类属性大写
        uppercase_attrs = {
            attr if attr.startswith("__") else attr.upper(): v
            for attr, v in attrs.items()
        }
        return type(kls, bases, uppercase_attrs)


class Example(metaclass=ExampleMeta):
    name = 'haha'



e = Example()
print(e.NAME)

# collections库 functiontools itertools
