"""
https://docs.python.org/zh-cn/3.8/library/functions.html
"""


def test_abs():
    """
    返回一个数的绝对值, 参数可以是一个整数或浮点数, 魔法函数 __abs__
    """
    assert abs(-1.2) == 1.2
    assert abs(-1) == 1


def test_all():
    """
    如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True
    """
    assert all(range(4)) is False
    assert all([]) is True


def test_any():
    """
    如果 iterable 的任一元素为真值则返回 True。 如果可迭代对象为空，返回 False
    """
    assert any(range(4)) is True
    assert any([]) is False


def test_bin():
    """
    将一个整数转变为一个前缀为“0b”的二进制字符串
    """
    assert bin(14) == "0b1110"
    assert bin(-14) == "-0b1110"
    # 格式化的写法
    assert f"{14:#b}" == "0b1110"


def test_bytes():
    """
    unicode是字符集
    utf8是编码方案 1-4个字节表示一个字符 汉字3个字符
    bytes就是二进制序列 可以理解为传输图片就是bytes格式 二进制流
    """
    # 空bytes
    assert bytes() == b''
    # 将字符串编码成bytes
    # @1
    assert bytes("我是中国人", "utf8") == b'\xe6\x88\x91\xe6\x98\xaf\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba'
    # @2
    assert "我是中国人".encode() == b'\xe6\x88\x91\xe6\x98\xaf\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba'
    # 可迭代对象转化为bytes
    assert bytes([1, 2, 3]) == b'\x01\x02\x03'
    # 空字节 字节数等于int
    assert bytes(1) == b'\x00'


def test_callable():
    """
    对象是否可调用
    """
    assert callable(print) is True


def test_chr():
    """
    unicode int对应的字符
    """
    assert chr(97) == 'a'


def test_classmethod():
    """
    classmethod类方法 实例和类都可以调用
    """

    class F:
        @classmethod
        def name(cls):
            return cls.__name__

    class S(F):
        pass

    f = F()
    s = S()
    assert F.name() == 'F'
    assert S.name() == 'S'
    assert f.name() == 'F'
    assert s.name() == 'S'


def test__class__():
    """
    __class__属性其实就是你是哪个类的实例 类的__class__就是他的元类
    """

    class MC(type):
        pass

    class C(metaclass=MC):
        pass

    assert C.__class__ == MC


def test_attrs():
    """
    属性
    """

    class C:
        pass

    a = C()
    setattr(a, 'name', 'deez')
    assert getattr(a, 'name') == 'deez'
    delattr(a, 'name')
    assert getattr(a, 'name', None) is None


def test_dict():
    """
    字典
    """
    d = dict(zip(range(5), range(5, 10)))
    assert d == {0: 5, 1: 6, 2: 7, 3: 8, 4: 9}


def test_dir():
    """
    如果没有实参，则返回当前本地作用域中的名称列表
    如果有实参，它会尝试返回该对象的有效属性列表
    如果对象有一个名为 __dir__() 的方法，那么该方法将被调用，并且必须返回一个属性列表
    如果对象不提供 __dir__()，这个函数会尝试从对象已定义的 __dict__ 属性和类型对象收集信息
    """

    class T:
        def __dir__(self):
            return 'area', 'perimeter', 'location'

    assert dir(T()) == ['area', 'location', 'perimeter']


def test_divmod():
    """
    整数除法时返回一对商和余数 q r
    """
    assert divmod(5, 3) == (1, 2)


def test_enumerate():
    """
    枚举可迭代对象 返回计数和元素
    """
    assert list(enumerate(range(3))) == [(0, 0), (1, 1), (2, 2)]


def test_eval():
    """
    一个字符串被解析求值 只能是单个表达式
    """
    assert eval('1+2') == 3


def test_exec():
    """
    动态执行代码
    """
    assert exec("""for i in range(5):
                print(i)
    """) is None


def test_filter():
    """
    从迭代元素中选择为True
    filter
    从迭代元素中选择为False
    itertools.filterfalse
    """
    assert list(filter(lambda x: x % 2, range(5))) == [1, 3]
    import itertools
    assert list(itertools.filterfalse(lambda x: x % 2, range(5))) == [0, 2, 4]


def test_float():
    """
    返回从数字或字符串 x 生成的浮点数
    """
    # 正无穷
    assert float('inf') > 1 << 63 - 1
    # 负无穷
    assert float('-inf') < -1 << 63
    # 保留小数点后2位
    assert f"{3.141:.2f}" == "3.14"


def test_frozenset():
    """
    不可变集合
    """
    assert frozenset([1, 2, 3, 2, 1]) == {1, 2, 3}


def test_globals():
    """
    返回表示当前全局符号表的字典。这总是当前模块的字典（在函数或方法中，不是调用它的模块，而是定义它的模块
    """
    print(globals())


def test_hash():
    """
    返回该对象的哈希值 __hash__()
    """


def test_hex():
    """
    返回小写16进制字符串
    """
    assert hex(255) == '0xff'
    assert f"{255:#x}" == '0xff'


def test_int():
    """
    返回一个基于数字或字符串 x 构造的整数对象，或者在未给出参数时返回 0
    """


def test_isinstance():
    """
    如果参数 object 是classinfo或者他子类的实例 返回 True
    """
    assert isinstance(0, int) is True


def test_issubclass():
    """
    如果 class 是 classinfo 的 (直接、间接或 虚拟) 子类则返回 True
    """

    class F:
        pass

    class S(F):
        pass

    assert issubclass(S, F) is True


def test_iter():
    """
    返回一个 iterator 对象 必须是支持迭代协议（有 __iter__() 方法）的集合对象，或必须支持序列协议（有 __getitem__() 方法，且数字参数从 0 开始
    """
    from collections.abc import Iterable, Iterator
    assert isinstance(iter(range(5)), Iterator) is True
    assert isinstance(range(5), Iterable) is True


def test_locals():
    """
    返更新并返回表示当前本地符号表的字典
    """
    print(locals())


def test_map():
    """
    接受和函数参数相同数量的可迭代对象 最短的可迭代对象耗尽则整个迭代就将结束
    """
    for i in map(lambda x, y: x + y, range(5), range(5, 10)):
        print(i)


def test_max():
    """
    返回可迭代对象中最大的元素，或者返回两个及以上实参中最大的
    :return:
    """
    assert max(range(10)) == 9
    assert max(1, 3, 2) == 3


def test_min():
    """
    返回可迭代对象中最小的元素，或者返回两个及以上实参中最小的
    :return:
    """
    assert min(range(10)) == 0
    assert min(1, 3, 2) == 1


def test_next():
    """
    通过调用 iterator 的 __next__() 方法获取下一个元素。如果迭代器耗尽，则返回给定的 default，如果没有默认值则触发 StopIteration。
    """

    def gen():
        for i in range(3):
            yield i

    g = gen()
    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 2
    assert next(g, None) is None


def test_oct():
    assert oct(8) == '0o10'
    assert f"{8:#o}" == '0o10'


def test_ord():
    """
    对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数
    """
    assert ord('a') == 97


def test_pow():
    """
    返回 base 的 exp 次幂；如果 mod 存在，则返回 base 的 exp 次幂对 mod 取余
    """
    assert pow(2, 2) == 4
    assert pow(2, 2, 3) == 1


def test_property():
    class T:
        def __init__(self, v, x):
            self._v = v
            self._x = x

        # 方式1
        @property
        def v(self): return self._v

        @v.setter
        def v(self, v): self._v = v

        @v.deleter
        def v(self): del self._v

        # 方式2
        def getx(self): return self._x

        def setx(self, x): self._x = x

        def delx(self): del self._x

        x = property(getx, setx, delx)


def test_repr():
    """
    返回包含一个对象的可打印表示形式的字符串
    """

    class T:
        def __repr__(self):
            return f"{self.__class__.__name__} instance"

    assert repr(T()) == 'T instance'


def test_reversed():
    """
    返回一个反向的 iterator。 seq 必须是一个具有 __reversed__() 方法的对象或者是支持该序列协议
    （具有从 0 开始的整数类型参数的 __len__() 方法和 __getitem__() 方法）
    """
    assert list(reversed(range(2))) == [1, 0]


def test_round():
    """
    返回 number 舍入到小数点后 n 位精度的值
    """
    assert round(3.1415) == 3
    assert round(3.1415, 2) == 3.14


def test_slice():
    sli = slice(3)
    s = "192.31.1.1"
    assert s[sli] == "192"


def test_sorted():
    """
    根据 iterable 中的项返回一个新的已排序列表
    """
    from functools import partial, cmp_to_key
    assert sorted(range(5), key=partial(pow, 2), reverse=True) == [4, 3, 2, 1, 0]
    assert sorted(range(5), key=cmp_to_key(lambda x, y: x - y)) == [0, 1, 2, 3, 4]


def test_staticmethod():
    """
    静态方法的调用可以在类上进行也可以在实例上进行
    """

    class T:
        @staticmethod
        def test():
            return 'test'

    t = T()
    assert T.test() == 'test'
    assert t.test() == 'test'


def test_sum():
    """
    从 start 开始自左向右对 iterable 的项求和并返回总计值
    """
    assert sum(range(5)) == 10
    # 拼接可迭代对象
    from itertools import chain
    assert sum(chain(range(5), range(5, 10))) == 45
    # 扩展精度
    import math
    assert math.fsum((0.123, 0.53, 0.22)) == 0.873


def test_type():
    """
    type 就是元类
    """
    X = type('X', (object,), dict(a=1))
    x = X()
    assert x.a == 1


def test_vars():
    """
    返回模块、类、实例或任何其它具有 __dict__ 属性的对象的 __dict__ 属性
    """
    print(vars(object))


def test_zip():
    """
    创建一个聚合了来自每个可迭代对象中的元素的迭代器
    """
    x = [1, 2, 3]
    y = [3, 4, 5, 6]
    # 以最短的为准
    assert list(zip(x, y)) == [(1, 3), (2, 4), (3, 5)]
    # 以最长的为准
    from itertools import zip_longest
    assert list(zip_longest(x, y, fillvalue=0)) == [(1, 3), (2, 4), (3, 5), (0, 6)]

