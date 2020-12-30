# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:51:26 2020

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        returnList = []
        
        if root == None: return returnList
        
        def traversal(node):
            returnList.append(node.val)
            if node.left != None:
                traversal(node.left)
            if node.right != None:
                traversal(node.right)
        traversal(root)
        return returnList