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

        
class Solution:
    def __init__(self):
        self.trie = Trie()
        self.node = self.trie.root
        self.checkNext = True
    def resetNode(self):
        self.node = self.trie.root
    def replaceWords(self, dictionary, sentence):
        
        # build dictionary
        for text in dictionary:
            self.trie.insert(text)
        
        # process sentence
        pointer = 0
        sentence_len = len(sentence)
        returnSentence = ""
        self.resetNode()
        while pointer != sentence_len:
            # process space
            if sentence[pointer] == " ":
                returnSentence += " "
                self.resetNode()
                self.checkNext = True
            else:
                # process word"
                cur_char = sentence[pointer]
                if self.checkNext and cur_char in self.node.child:
                    self.node = self.node.child[cur_char]
                    returnSentence += cur_char
                    if self.node.isEndOfWord:
                        # after should be replace
                        while pointer+1 != sentence_len and sentence[pointer+1] != " ":
                            pointer+=1
                else:
                    self.checkNext = False
                    returnSentence += cur_char
                
            pointer += 1
        return returnSentence
                        
                            
               
                   
            
sol = Solution()

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"

dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"

dictionary = ["catt","cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
dictionary = ["ac","ab"]
sentence = "it is abnormal that this solution is accepted"
ans = sol.replaceWords(dictionary, sentence)                
print(ans)
        
                
                
        