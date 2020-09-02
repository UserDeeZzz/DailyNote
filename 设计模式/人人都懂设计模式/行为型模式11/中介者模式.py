"""中介者模式 用一个中介对象来封装一系列的对象交互，中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。"""


class ChatRoom:

    def __init__(self, name):
        self.name = name

    def show_message(self, user, message):
        print(f"{self.name}>>{user}:{message}")


class User:

    def __init__(self, name):
        self._name = name
        self.chat_room = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name

    def join_chat_room(self, chat_room):
        self.chat_room = chat_room

    def send_message(self, message):
        if self.chat_room is None:
            print("您还未加入聊天室")
        else:
            self.chat_room.show_message(self, message)


if __name__ == '__main__':
    u1 = User("u1")
    u2 = User("u2")
    c = ChatRoom("老年活动室")
    u1.join_chat_room(c)
    u2.join_chat_room(c)
    u1.send_message("How are you?")
    u2.send_message("I'm fine.")
