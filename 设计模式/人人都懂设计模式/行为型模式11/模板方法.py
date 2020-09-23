"""
将算法分步骤 然后依次让子类填充
"""
from abc import ABC, abstractmethod


class Algorithm(ABC):

    def template(self):
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self):
        print("基本步骤1")

    def base_operation2(self):
        print("基本步骤2")

    def base_operation3(self):
        print("基本步骤3")

    @abstractmethod
    def required_operations1(self):
        pass

    @abstractmethod
    def required_operations2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass


class AlgorithmImpl(Algorithm):

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")