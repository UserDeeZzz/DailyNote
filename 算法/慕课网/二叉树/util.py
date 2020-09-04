class Node:

    def __init__(self, v):
        self.left = None
        self.right = None
        self.value = v

    def __str__(self):
        resp = ""
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node is not None:
                resp += str(node.value) + '\n'
                queue.append(node.left)
                queue.append(node.right)
        return resp


def binary_tree(data):
    if not data:
        return None

    root = Node(data.pop(0))
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node is not None:
            l_data = data.pop(0)
            r_data = data.pop(0)
            left = Node(l_data) if l_data is not None else None
            right = Node(r_data) if r_data is not None else None
            node.left, node.right = left, right
            queue.append(left)
            queue.append(right)
    return root


bt = binary_tree([12, 5, 18, 2, 9, 15, 19, None, None, None, None, None, 17, None, None, 16, None, None, None])

if __name__ == '__main__':
    print(bt)
