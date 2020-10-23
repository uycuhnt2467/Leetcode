# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:38:40 2020

@author: a8520
"""


class TrieNode:
    
    def __init__(self, char):
        self.data = char
        self.value = 0
        self.child = {}
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode("@")
    def insert(self, word, value):
        node = self.root
        
        for char in word:
            if char in node.child:
                node = node.child[char]
                node.value += value
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.child[char] = new_node
                node = new_node
                node.value += value
            
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.node = self.trie.root
 
    def reset(self):
        self.node = self.trie.root
        
    def insert(self, key, val):
        if key not in self.dict_insert:
            self.dict_insert[key] = val
        else:
            oldVal = self.dict_insert[key]
            diff = val - oldVal
            self.dict_insert[key] = val
            val = diff
        self.trie.insert(key, val)

    def sum(self, prefix):
        pointer = 0
        self.reset()
        node = self.node
        while pointer != len(prefix):
            
            if (len(node.child) != 0) and  prefix[pointer] in node.child:
                node = node.child[prefix[pointer]]
                pointer += 1
            else:
                break
        if pointer == len(prefix):
            return node.value
        else:
            return 0                
            
        

obj = MapSum()
key, val = "apple", 3
obj.insert(key,val)
prefix = "ap"
param_2 = obj.sum(prefix)
key, val = "app", 2
obj.insert(key,val)
prefix = "ap"
param_2 = obj.sum(prefix)      