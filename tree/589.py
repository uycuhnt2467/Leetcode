# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 09:21:19 2020

@author: a8520
"""


# Definition for a Node.
"""
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        returnList = []
        stack = []
        if root == None:
            return []
        
        visited = set()
        
        stack.append(root)
        while len(stack) != 0:
            # print("stack", stack)
            # print("visited", visited)
            cur = stack[-1]
            if cur not in visited:
                # print("cur not in visited")
                visited.add(cur)
                returnList.append(cur.val)
            if cur.children != None:
                count = 0
                for childrenNode in cur.children:
                    if childrenNode not in visited:
                        # print(childrenNode)
                        stack.append(childrenNode)
                        # print("here")
                        break
                    else:
                        count += 1
                if count == len(cur.children):
                    stack.pop()
            else:
                # no children
                stack.pop()
        return returnList