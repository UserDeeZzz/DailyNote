from util import bt


def pre_order(tree):
    stack = [tree]
    while stack:
        node = stack.pop(-1)
        if node is not None:
            print(node.value)
            stack.append(node.right)
            stack.append(node.left)


def mid_order(tree):
    stack = []
    current = tree
    while current or stack:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            node = stack.pop(-1)
            print(node.value)
            current = node.right


def post_order(tree):
    stack = []
    output = []
    current = tree
    while current or stack:
        if current is not None:
            stack.append(current)
            output.append(current.value)
            current = current.right
        else:
            node = stack.pop(-1)
            current = node.left

    print(output[-1::-1])


if __name__ == '__main__':
    post_order(bt)
