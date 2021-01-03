# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 12:19:39 2021

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        returnList = list()
        def findLeaf(node, temp_sum , temp_list):
            if node == None:
                pass
            else:
                temp_list.append(node.val)
                if node.val == temp_sum and node.left == None and node.right == None:
                    returnList.append(temp_list[:])
                else:
                    findLeaf(node.left, temp_sum - node.val, temp_list)
                    findLeaf(node.right, temp_sum - node.val, temp_list)
                temp_list.pop()
        if root == None:
            return []
        findLeaf(root, sum, [])
        return returnList