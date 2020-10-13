from threading import Timer


def target():
    print("schedule target")


t = Timer(10, target)
t.start()
