class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        t=-1
        mx=float('-inf')
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if t==-1:
                    t=i
                else:
                    return False
        print(t)
        if t==-1:
            return True
        if t == 1 or nums[t - 2] <= nums[t]:  
            nums[t - 1] = nums[t]
        else:
            nums[t] = nums[t - 1]
            # print(nums,sorted(nums))
        if nums!=sorted(nums):
            return False
        return True
