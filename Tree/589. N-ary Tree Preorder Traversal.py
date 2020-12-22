class Solution:
  def preorder(self, root: 'Node') -> List[int]:
    """ do it iteratively """
    if root is None:
      return []
    stack, ans = [root], []            
    while stack:
      root = stack.pop()
      ans.append(root.val)
      stack.extend(root.children[::-1])    
    return ans