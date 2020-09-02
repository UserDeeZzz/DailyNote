"""动态地给一个对象添加一些额外的职责。就增加功能来说，装饰器模式相比生成子类更为灵活"""


def italic(f):
    def _inner(*args, **kwargs):
        resp = f(*args, **kwargs)
        return f"<i>{resp}</i>"

    return _inner


def bold(f):
    def _inner(*args, **kwargs):
        resp = f(*args, **kwargs)
        return f"<b>{resp}</b>"

    return _inner


@italic
@bold
def text(mes):
    return mes


if __name__ == '__main__':
    print(text("deez"))
