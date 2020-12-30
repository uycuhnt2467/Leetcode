# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:15:18 2020

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
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        returnList = list()
        next_ = []
        next_.append([root])
        while len(next_) != 0:
            cur = next_.pop(0)
            now = list()
            for i in cur:
                now.append(i.val)
            returnList.append(now)
            next_layer = list()
            for i in cur:
                if (i.children != None):
                    for j in i.children:
                        if j != None:
                            next_layer.append(j)
            if len(next_layer) != 0:
                next_.append(next_layer)
        return returnList
        
        
        