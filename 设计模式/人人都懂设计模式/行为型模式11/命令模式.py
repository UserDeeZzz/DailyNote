class DeleteFileCommand:

    def __init__(self):
        self._files = []

    def execute(self, fn):
        self._files.append(fn)
        print(f"deleting {fn}")

    def undo(self):
        if self._files:
            fn = self._files.pop()
            print(f"restoring {fn}")
        else:
            print(f"no delete file")


class Invoker:

    def __init__(self, command):
        self._command = command

    def on_do_press(self, fn):
        self._command.execute(fn)

    def on_undo_press(self):
        self._command.undo()


def main():
    """
    >>> cmd = DeleteFileCommand()
    >>> iv = Invoker(cmd)
    >>> iv.on_do_press('test.py')
    deleting test.py
    >>> iv.on_undo_press()
    restoring test.py
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
