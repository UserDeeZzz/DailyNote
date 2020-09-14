class Facade:
    def __init__(self):
        self.connector = Connector
        self.cache = Cache()
        self.parser = Parser()
        self.optimizer = Optimizer()
        self.executor = Executor()

    def handle(self, sql):
        self.connector.handle()
        self.cache.handle(sql)
        self.parser.handle(sql)
        self.optimizer.handle(sql)
        self.executor.handle(sql)


class Connector:
    @staticmethod
    def handle():
        print("建立线程连接")


class Cache:
    @staticmethod
    def handle(sql):
        print(f"查询{sql}缓存是否命中")


class Parser:
    @staticmethod
    def handle(sql):
        print(f"解析{sql}语义语法词法")


class Optimizer:
    @staticmethod
    def handle(sql):
        print(f"优化{sql}查询")


class Executor:
    @staticmethod
    def handle(sql):
        print(f"执行查询{sql}语句")


if __name__ == '__main__':
    f = Facade()
    f.handle("SELECT * FROM `test`")
