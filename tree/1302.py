# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 10:40:51 2020

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        stack = []
        stack.append([root])
        sum_layer = 0
        layer = 0
        while stack:
            current_layer = stack.pop()
            next_layer = list()
            for node in current_layer:
                if node.left != None:
                    next_layer.append(node.left)
                if node.right != None:
                    next_layer.append(node.right)
            if len(next_layer) == 0:
                return sum_layer
            else:
                sum_layer = 0
                # print("nx lay", len(next_layer))
                for proc_node in next_layer:
                    sum_layer += proc_node.val
            stack.append(next_layer)
            layer += 1