"""责任链模式 避免请求发送者与接收者耦合在一起，让多个对象都有可能接收请求，将这些对象连接成一条链，并且沿着这条链传递请求，直到有对象处理它为止"""
from abc import ABCMeta


class Handler(metaclass=ABCMeta):

    def __init__(self,name):
        self.name = name
        self.next = None

    def handle(self,request):
        if self.next is not None:
            print(f"{self.name}-{request}->{self.next.name}")
            self.next.handle(request)
        else:
            print(f"{self.name}-{request}->end")


if __name__ == '__main__':
    supervisor = Handler('Supervisor')
    ceo = Handler('CEO')
    supervisor.next = ceo

    supervisor.handle("请年假5天......")