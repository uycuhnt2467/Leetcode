class TrieNode:
    
    def __init__(self, char):
        self.data = char
        self.isEndOfWord = False
        self.child = {}
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode("@")
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char in node.child:
                node = node.child[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.child[char] = new_node
                node = new_node
            
        node.isEndOfWord = True
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.node = self.trie.root
 
    # def reset(self):
    #     self.node = self.trie.root

    def buildDict(self, dictionary):
        for text in dictionary:
            self.trie.insert(text)
        
    def search(self, searchWord):
        node = self.node
        return self.checkInTrie(searchWord, node, 1)
    
    def checkInTrie(self, subword, node, remain):
        if not subword:
            return True if remain == 0 and node.isEndOfWord else False
        for key in node.child.keys():
            if key == subword[0]:
                if self.checkInTrie( subword[1:],node.child[key],remain):
                    return True
            elif remain == 1:
                if self.checkInTrie( subword[1:],node.child[key],0):
                    return True
        return False
                
            
        
    
# Your MagicDictionary object will be instantiated and called as such:
            
dictionary = ["hello", "hallo", "leetcode"]
searchWord = "haallo"
test = MagicDictionary()
test.buildDict(dictionary)
param_2 = test.search(searchWord)