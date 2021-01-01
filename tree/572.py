# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 23:10:31 2021

@author: a8520
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # step 1: find root node
        # step 2: traverse and compare whether the result is similar
        
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
        
        queue = [s]
        while queue:
            cur = queue.pop(0)
            
            if cur.val == t.val:
                if inOrderCheck(cur, t):
                    return True
            if cur.left != None:
                queue.append(cur.left)
            if cur.right != None:
                queue.append(cur.right)
        return False
                
        
                
        