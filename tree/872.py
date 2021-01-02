# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 09:44:41 2021

@author: a8520
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf_first = []
        leaf_second = []
        def findLeaf(node, select):
            if node == None:
                pass
            else:
                if node.left == None and node.right == None:
                    if select == 0:
                        leaf_first.append(node.val)
                    else:
                        leaf_second.append(node.val)
                elif node.left == None:
                    findLeaf(node.right, select)
                elif node.right == None:
                    findLeaf(node.left, select)
                else:
                    findLeaf(node.left, select)
                    findLeaf(node.right, select)
        findLeaf(root1, 0)
        findLeaf(root2, 1)
        
        if len(leaf_first) != len(leaf_second):
            return False
        else:
            for i in range(len(leaf_first)):
                if leaf_first[i] != leaf_second[i]:
                    return False
            return True
        
        