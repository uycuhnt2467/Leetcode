# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 23:39:58 2021

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        queue = [[root]]
        
        while queue:
            curLevel = queue.pop(0)
            next_level_node = list()
            next_level = list()
            for node in curLevel:
                next_level.append(node.val)
                if node.left != None:
                    next_level_node.append(node.left)
                if node.right != None:
                    next_level_node.append(node.right)
            res.append(next_level)
            if len(next_level_node) > 0:
                queue.append(next_level_node)
        return res