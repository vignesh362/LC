import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        hqNum=[]
        for i,j in enumerate(nums):
            hqNum.append((j,i))
        heapq.heapify(hqNum)
        # print(hqNum)
        marked=set()
        res=0
        while len(marked)!=len(nums):
            j,i=heapq.heappop(hqNum)
            if i not in marked:
                marked.add(i)
                res+=j
                # print(i,j)
                if i-1>=0:
                    marked.add(i-1)
                if i+1<len(nums):
                    marked.add(i+1)
        return res


        