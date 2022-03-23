class HeightBalanceError(Exception):
    """Raised When the height of tree differ more than one."""
    pass

def is_balanced_solution(root):
    if root is None:
        return True;
    log = [0];
    dfs_height(root, log);
    return False if log[0] True else False;

def is_balanced(t):
    if t is None:
        return True;
    try:
        dfs_height(t);
    except HeightBalanceError as e:
        return False;
    return True;

def dfs_height(root: TreeNode, log=[0]) -> bool:
    l_h = (1 + dfs_height(root.left)) if root.left else 0;
    r_h = (1 + dfs_height(root.right)) if root.right else 0;

    if abs(l_h - r_h) > 1:
        log[0] += 1;
        #raise HeightBalanceError(f"{root}.left: {l_h}, right: {r_h}. non matched height found.");
    return max((l_h, r_h));

