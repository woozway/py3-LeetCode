"""
1. Clarification
2. Possible solutions
 - recursion
 - dfs
3. Coding
4. Tests
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T=O(n), S=O(h)
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right: return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


# # T=O(n), S=O(h)
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if not root: return False
#         que_node = collections.deque([root])
#         que_val = collections.deque([root.val])
#         while que_node:
#             now = que_node.popleft()
#             temp = que_val.popleft()
#             if not now.left and not now.right:
#                 if temp == targetSum:
#                     return True
#                 continue
#             if now.left:
#                 que_node.append(now.left)
#                 que_val.append(now.left.val + temp)
#             if now.right:
#                 que_node.append(now.right)
#                 que_val.append(now.right.val + temp)
#         return False
