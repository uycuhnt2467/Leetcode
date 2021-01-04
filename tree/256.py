# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 08:51:08 2021

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        else:
            if root.val == p.val or root.val == q.val:
                return root
            else:
                left = self.lowestCommonAncestor(root.left, p, q)
                right = self.lowestCommonAncestor(root.right, p, q)
                if left != None and right != None:
                    return root
                else:
                    return left or right or None