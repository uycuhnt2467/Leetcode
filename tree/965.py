# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 23:25:22 2021

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return False
        
        uni_value = root.val
        
        def checkValue(node):
            if node == None:
                return True
            elif node.val == uni_value:
                return True and checkValue(node.left) and checkValue(node.right)
            else:
                return False
        return checkValue(root)
        