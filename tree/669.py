# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:36:37 2021

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        def checkNode(node):
            if node == None:
                return node
            
            node.left = checkNode(node.left)
            node.right = checkNode(node.right)
            
            if node.left != None and node.right != None:
                if node.val > high:
                    return None
                elif node.val < low:
                    return None
                else:
                    return node
            elif node.left != None:
                if node.val > high:
                    return node.left
                elif node.val < low:
                    return node.left
                else:
                    return node
            elif node.right != None:
                if node.val > high:
                    return node.right
                elif node.val < low:
                    return node.right
                else:
                    return node
            else:
                # both children are None
                if node.val > high:
                    return None
                elif node.val < low:
                    return None
                else:
                    return node
        return checkNode(root)