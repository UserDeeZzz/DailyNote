from util import bt


def pre_order(tree):
    if tree is None:
        return
    print(tree.value)
    pre_order(tree.left)
    pre_order(tree.right)


def mid_order(tree):
    if tree is None:
        return
    mid_order(tree.left)
    print(tree.value)
    mid_order(tree.right)


def post_order(tree):
    if tree is None:
        return
    mid_order(tree.left)
    mid_order(tree.right)
    print(tree.value)


if __name__ == '__main__':
    t = bt
    mid_order(bt)
