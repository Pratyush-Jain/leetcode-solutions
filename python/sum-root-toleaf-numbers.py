# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sumt = 0
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.dfs(root,0)
        return self.sumt
        
    def dfs(self,root,val):
        if root is None:
            return
        val= val*10 + root.val
        if(root.left is None and root.right is None):
            self.sumt += val
            return
        self.dfs(root.left,val)
        self.dfs(root.right,val)
        
