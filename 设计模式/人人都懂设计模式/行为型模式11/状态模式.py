"""状态模式 允许对象在内部状态发生改变时改变它的行为"""
from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):

    def __init__(self):
        self.states = []
        self._current_state = None
        self._state_info = None

    def add_state(self, state):
        self.states.append(state)

    def change_state(self, state):
        self._current_state = state

    def get_state(self):
        return self._current_state

    def set_state_info(self, static_info):
        self._state_info = static_info
        for state in self.states:
            if state.is_match(static_info):
                self.change_state(state)

    def get_state_info(self):
        return self._state_info

    def behavior(self):
        if self._current_state is not None:
            self._current_state.behavior()


class State(metaclass=ABCMeta):

    def __init__(self):
        self.name = None

    @abstractmethod
    def behavior(self):
        pass

    @abstractmethod
    def is_match(self, state_info):
        pass

    def get_name(self):
        return self.name


class Solid(State):

    def __init__(self):
        super().__init__()
        self.name = "solid"

    def behavior(self):
        print(f"{self.name}:坚硬")

    def is_match(self, state_info):
        return state_info < 0


class Liquid(State):

    def __init__(self):
        super().__init__()
        self.name = "liquid"

    def behavior(self):
        print(f"{self.name}:柔软")

    def is_match(self, state_info):
        return 0 < state_info < 100


class Gas(State):
    def __init__(self):
        super().__init__()
        self.name = "gas"

    def behavior(self):
        print(f"{self.name}:缥缈")

    def is_match(self, state_info):
        return state_info >= 100


class Water(Context):
    pass


if __name__ == '__main__':
    water = Water()
    gas = Gas()
    liquid = Liquid()
    solid = Solid()
    water.add_state(gas)
    water.add_state(liquid)
    water.add_state(solid)
    water.set_state_info(100)
    water.behavior()
