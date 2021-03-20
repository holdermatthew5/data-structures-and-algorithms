def intersection(tree1, tree2):
    temp1 = []
    temp2 = []
    def traverse1(node, tree):
        if tree == 1:
            temp1.append(node.value)
        else:
            temp2.append(node.value)
        if node.left:
            traverse1(node.left, tree)
        if node.right:
            traverse1(node.right, tree)

    def traverse2(node1, node2):
        temp1.append(node1.value)
        temp2.append(node2.value)
        if node1.left and node2.left:
            traverse2(node1.left, node2.left)
        elif node1.left:
            traverse1(node1.left, 1)
        elif node2.left:
            traverse1(node2.left, 2)
        if node1.right and node2.right:
            traverse2(node1.right, node2.right)
        elif node1.right:
            traverse1(node1.right, 1)
        elif node2.right:
            traverse1(node2.right, 2)
    traverse2(tree1.root, tree2.root)
    if len(temp1) >= len(temp2):
        return [value for value in temp1 if value in temp2]
    else:
        return [value for value in temp2 if value in temp1]