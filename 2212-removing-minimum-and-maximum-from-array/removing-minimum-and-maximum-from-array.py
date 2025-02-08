class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn,mx=float('inf'),float('-inf')
        mnl,mxl=-1,-1
        n=len(nums)
        for i in range(n):

            if nums[i]>mx:
                mx=nums[i]
                mxl=i
            if nums[i]<mn:
                mn=nums[i]
                mnl=i

        if mnl>mxl:
            mxl,mnl=mnl,mxl
        left_deletions = mxl + 1
        right_deletions = n - mnl
        split_deletions = (mnl + 1) + (n - mxl)
        
        return min(right_deletions,split_deletions,left_deletions)


        