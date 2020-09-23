"""
将数据结构和操作分离 复合数据结构遍历 根据不同元素采用不同的操作
"""


class Node:
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor:
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth = getattr(self, 'visit_' + cls.__name__, None)
            if meth:
                break
        if not meth:
            meth = self.generic_visit
        meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print(f"generic_visit {node.__class__.__name__}")

    def visit_B(self, node, *args, **kwargs):
        print(f"visit_B {node.__class__.__name__}")


def main():
    """
    >>> a, b, c = A(), B(), C()
    >>> visitor = Visitor()
    >>> visitor.visit(a)
    generic_visit A
    >>> visitor.visit(b)
    visit_B B
    >>> visitor.visit(c)
    visit_B C
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
