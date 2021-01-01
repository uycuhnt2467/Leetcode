# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #  level order traversal
        
        if root == None:
            return 0
        
        queue = [[root]]
        level_val = 1
          
        while queue:
            next_level = []
            cur_level = queue.pop(0)
            for node in cur_level:
                if node.left == None and node.right == None:
                    return level_val
                elif node.left == None:
                    next_level.append(node.right)
                elif node.right == None:
                    next_level.append(node.left)
                else:
                    next_level.append(node.left)
                    next_level.append(node.right)
            level_val += 1
            queue.append(next_level)
            
            
        