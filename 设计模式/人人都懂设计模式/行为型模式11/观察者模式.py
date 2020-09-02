"""观察者模式 定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新"""
from abc import ABCMeta, abstractmethod


class Observable(metaclass=ABCMeta):
    def __init__(self):
        self.observers = []

    def add(self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        self.observers.remove(observer)

    def notify(self, mes):
        for o in self.observers:
            o.update(self, mes)

    @abstractmethod
    def change(self, d):
        pass


class ObservableImpl(Observable):
    def __init__(self):
        super().__init__()
        self._data = 0

    def change(self, d):
        self._data = d
        if self._data == 100:
            mes = "水烧开了！！"
            self.notify(f"{self}{mes}")


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, observable, mes):
        pass


class ObserverImpl(Observer):

    def update(self, observable, mes):
        # 推模型 推送消息
        # 拉模型 推送连接
        print(f"{observable}:{mes}")


if __name__ == '__main__':
    obs = ObservableImpl()
    ob = ObserverImpl()
    obs.add(ob)
    obs.change(100)
