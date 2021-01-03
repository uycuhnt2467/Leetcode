# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 22:42:37 2021

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum_record = [0]
        
        def dfs(node, cum, sum_):
            next_cum = cum * 10 + node.val
            if node.left == None and node.right == None:
                sum_[0] += next_cum
            else:
                if node.left != None:
                    dfs(node.left, next_cum,sum_)
                if node.right != None:
                    dfs(node.right, next_cum,sum_)
        if root == None:
            return 0
        dfs(root, 0, sum_record)
        return sum_record[0]