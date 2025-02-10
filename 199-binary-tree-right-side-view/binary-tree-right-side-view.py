# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        
        res=[]

        level=[root]

        while level:
            temp=[]
            res.append(level[0].val)
            for i in level:
                if i.right:
                    temp.append(i.right)
                if i.left:
                    temp.append(i.left)
            level=temp[:]
        return res
            





        