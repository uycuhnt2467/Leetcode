# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 08:04:09 2020

@author: a8520
"""


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        returnList = []
        def traversal(node):
            if node.left != None:
                traversal(node.left)
            if node.right != None:
                traversal(node.right)
            returnList.append(node.val)
        traversal(root)
        return returnList