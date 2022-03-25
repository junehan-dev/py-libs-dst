from tree_node import TreeNode

def dfs_get_height(root: TreeNode, log=[0]) -> tuple:
    l_h = (1 + max(dfs_get_height(root.left))) if root.left is not None else 0;
    r_h = (1 + max(dfs_get_height(root.right))) if root.right is not None else 0;
   
    return (l_h, r_h);
        #raise HeightBalanceError(f"{root}.left: {l_h}, right: {r_h}. non matched height found.");

