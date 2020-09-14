"""代理对象可以在客户端和目标对象之间起到中间调和的作用，并且可以通过代理对象隐藏不希望被客户端看到的内容和服务，或者添加客户需要的额外服务"""
# 火车票 飞机票代售软件
from abc import abstractmethod, ABCMeta


class Subject(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @abstractmethod
    def request(self, content=''):
        pass


class ProxySubject(Subject):
    def __init__(self, name, subject):
        super().__init__(name)
        self._real_subject = subject

    @staticmethod
    def pre_request():
        print("pre_request......")

    def request(self, content=''):
        self.pre_request()
        if self._real_subject is not None:
            self._real_subject.request(content)
        self.after_request()

    @staticmethod
    def after_request():
        print("after_request......")


class RealSubject(Subject):
    def request(self, content=''):
        print(f"{self.get_name()}:请求内容为{content}")


class Client:
    @staticmethod
    def request_subject(sub, content):
        if isinstance(sub, Subject):
            sub.request(content)
        else:
            print("请求主题不合法")


if __name__ == '__main__':
    c = Client()
    real_sub = RealSubject("真实主题")
    sub = ProxySubject("代理", real_sub)
    c.request_subject(sub, "hello world")
