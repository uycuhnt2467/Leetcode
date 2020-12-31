# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:17:34 2020

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
   
        def inOrderCheck(root1, root2):
            if root1 == None and root2 == None:
                return True
            elif root1 == None:
                return False
            elif root2 == None:
                return False
            else:
                if root1.val == root2.val:
                    return inOrderCheck(root1.left, root2.left) and inOrderCheck(root1.right, root2.right)
                else:
                    return False
        return inOrderCheck(p, q)