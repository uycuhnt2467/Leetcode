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
 
    def reset(self):
        self.node = self.trie.root

    def buildDict(self, dictionary):
        for text in dictionary:
            self.trie.insert(text)
        
    def search(self, searchWord):
        self.reset()
        pointer = 0
        search_word_len = len(searchWord)
        while pointer != search_word_len:
            if pointer == search_word_len-1:
                for next_node in self.node.child:
                    print(next_node)
                    if next_node != searchWord[pointer] and self.node.child[next_node].isEndOfWord:
                        return True
                return False
            elif searchWord[pointer] in self.node.child:
                self.node = self.node.child[searchWord[pointer]]
                pointer += 1
            else:
                for incorrect_node in self.node.child:
                    remain_word = searchWord[pointer+1:]
                    if (self.checkInTrie(remain_word, self.node.child[incorrect_node]) == True):
                        return True
                return False
            
        return False
    def checkInTrie(self, subword, incorrect_node):
        cur_node = incorrect_node
        sub_pointer = 0
        subword_len = len(subword)
        while sub_pointer != subword_len:
            # print(subword[sub_pointer])
            # print(cur_node.child)
            if subword[sub_pointer] in cur_node.child:
                cur_node = cur_node.child[subword[sub_pointer]]
                sub_pointer += 1
            else:
                return False
        if cur_node.isEndOfWord:
            return True
        else:
            return False
                
            
        
    
# Your MagicDictionary object will be instantiated and called as such:
            
dictionary = ["hello", "hallo", "leetcode"]
searchWord = "hello"
test = MagicDictionary()
test.buildDict(dictionary)
param_2 = test.search(searchWord)