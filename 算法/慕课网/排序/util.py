import random

def random_list():
    resp = [i for i in range(100)]
    random.shuffle(resp)
    return resp


