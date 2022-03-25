def left_rotate(root):
    pass
    predecessor = root.right;
    root.right = predecessor.left;
    predecessor.val, root.val = root.val, predecessor.val
    return (root);

def right_rotate(root):
    pass
    predecessor = root.left;
    predecessor.val, root.val = root.val, predecessor.val
    root.left = predecessor.right;
    return (root);
