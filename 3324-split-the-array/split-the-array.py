import collections
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        # res1=[]
        # res2=[]
        # i=0
        # for i in range(len(nums)):
        #     if len(res1)==len(nums)//2:
        #         break
        #     temp=nums[i]
        #     if temp not in t1:
        #         res1.append(temp)
        #     else:
        #         res2.append(temp)
        t=collections.Counter(nums)
        print(t)
        for i in t.keys():
            if t[i]>2:
                return False
        return True
            
    
        