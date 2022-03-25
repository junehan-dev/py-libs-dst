class HeightBalanceError(Exception):
    """Raised When the height of tree differ more than one."""
    pass

def is_balanced(t):
    if t is None:
        return True;
    l_h, r_h = dfs_get_l_r_h(t);
    return False if abs(l_h - r_h) > 1 else False;

def dfs_get_h(root) -> bool:
        #raise HeightBalanceError(f"{root}.left: {l_h}, right: {r_h}. non matched height found.");
    return max(dfs_get_l_r_h(root));

def dfs_get_l_r_h(root) -> tuple:
    l_h = (1 + max(dfs_get_l_r_h(root.left))) if root.left is not None else 0;
    r_h = (1 + max(dfs_get_l_r_h(root.right))) if root.right is not None else 0;
   
    return (l_h, r_h);
        #raise HeightBalanceError(f"{root}.left: {l_h}, right: {r_h}. non matched height found.");

