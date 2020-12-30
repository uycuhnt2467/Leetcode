# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:01:40 2020

@author: a8520
"""


# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2
# Input: root = []
# Output: []

# Example 3
# Input: root = [1]
# Output: [1]

# Example 4
# Input: root = [1,2]
# Output: [2,1]

# Example 5
# Input: root = [1,null,2]
# Output: [1,2]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # def getLeft(i):
        #     return i * 2 + 1
        # def getRight(i):
        #     return i * 2 + 2
        
        # returnList = list()
        
        # last = len(root)
        # def traversal(i):
        #     if (root[i] != None):
        #         returnList.append(root[i])
        #     if getLeft(i) < last:
        #         traversal(getLeft(i))
            
        #     if getRight(i) < last:
        #         traversal(getRight(i))
        # traversal(0)
        # return returnList
        returnList = list()
        def traversal(node):
            if node.left != None:
                traversal(node.left)
            
            returnList.append(node.val)
            if node.right != None:
                traversal(node.right)
        if (root == None):
            return []
        traversal(root)
        return returnList

sol = Solution()

root = [1,None,2]
Output: [1,2]

print(sol.inorderTraversal(root)
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        