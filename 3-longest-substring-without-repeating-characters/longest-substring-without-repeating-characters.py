class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1 or len(set(s))==1:
            return 1  
        left,right=0,1
        mx=0
        def overRide():
            nonlocal mx
            temp=right-left
            if temp>mx:
                # print(s[left:right])
                # print(left,right)
                # print(s[left:right+1])
                mx=temp
            
        for i in range(1,len(s)):
            print(i)
            print(s[left:right])
            print(mx)
            if s[i] not in s[left:right]:
                # print(s[i],s[left:right])
                right+=1
                # print("---")
                overRide()
            else:
                while s[left]!=s[i]:
                    left+=1
                left+=1
                right+=1
                # print("---+--")
                overRide()
        return mx



        



        