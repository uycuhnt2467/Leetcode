# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 10:12:26 2020

@author: a8520
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = []
        returnList = []
        
        if root == None:
            return returnList
        
        stack.append([root])
        
        while root or stack:
            if root != None:
                children = root.children
                if children != None and len(children) > 0:
                    stack.append(children)
                    root = children[0]
                else:
                    root = None
            else:
                prev = stack.pop()
                proc = prev.pop(0)
                returnList.append(proc.val)
                if prev:
                    stack.append(prev)
                    root = prev[0]
                else:
                    root = None
        return returnList
                
            
        