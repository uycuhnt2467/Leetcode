# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
       
        tempList= [root]
        start = [0]
        next_layer_len = len(tempList)
        cur_layer = 0
        
        while next_layer_len != 0:
            start.append((start[cur_layer] + next_layer_len))
            next_layer_len = 0
            cur_end = len(tempList)
            for i in range(start[cur_layer], cur_end):
                if tempList[i].left != None:
                    tempList.append(tempList[i].left)
                    next_layer_len += 1
                if tempList[i].right != None:
                    tempList.append(tempList[i].right)
                    next_layer_len += 1
            cur_layer += 1
        
        returnList = list()
        
        for j in range(len(start) - 2, -1, -1):
            start_ = start[j]
            end_ = start[j + 1]
            layer = []
            while start_ < end_:
                layer.append(tempList[start_].val)
                start_ += 1
            returnList.append(layer)
        return returnList
            
            
        