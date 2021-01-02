# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def checkNode(node):
            if node == None:
                return node
            
            if node.left != None and node.right != None:
                node.left = checkNode(node.left)
                node.right = checkNode(node.right)
            elif node.left != None:
                node.left = checkNode(node.left)
            elif node.right != None:
                node.right = checkNode(node.right)
            else:
                # both None
                pass
            if node.left == None and node.right == None and node.val == 0:
                return None
            else:
                return node
        return checkNode(root)