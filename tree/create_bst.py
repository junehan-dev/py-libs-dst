from tree_node import TreeNode

def create_bst(sorted_arr):
    assert(sorted_arr);
    root = TreeNode(sorted_arr[len(sorted_arr) // 2]);
    create_bst_dfs(root, sorted_arr) if len(sorted_arr) > 1 else None;
    return root;

def create_bst_dfs(parent, sorted_arr):
    if len(sorted_arr) < 2:
        return None;

    mid = len(sorted_arr) // 2;
    l_arr = sorted_arr[:mid];
    parent.left = TreeNode(l_arr[len(l_arr) // 2]);
    create_bst_dfs(parent.left, l_arr);
    r_arr = sorted_arr[mid+1:];
    if r_arr:
        parent.right = TreeNode(r_arr[len(r_arr) // 2]);
        create_bst_dfs(parent.right, r_arr);

from collections import deque

def create_bst_bfs(sorted_arr):
    assert(sorted_arr);
    root = TreeNode(sorted_arr[len(sorted_arr) // 2]);
    q_subtree = deque([(root, sorted_arr)]);

    while q_subtree:
        parent, sorted_arr = q_subtree.popleft();
        left = len(sorted_arr);
        mid = left // 2;
        if left > 1:
            l_arr = sorted_arr[:mid];
            parent.left = TreeNode(l_arr[len(l_arr) // 2]);
            q_subtree.append((parent.left, l_arr));
        if left > 2:
            r_arr = sorted_arr[mid+1:];
            parent.right = TreeNode(r_arr[len(r_arr) // 2]);
            q_subtree.append((parent.right, r_arr));

    return root;

