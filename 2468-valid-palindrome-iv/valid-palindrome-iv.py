class Solution:
    def makePalindrome(self, s: str) -> bool:
        
        t=s[::-1]
        ct=0
        if t==s:
            return True
        for i in range(len(s)//2):
            if t[i]!=s[i]:
                ct+=1
        print(t)
        print(ct)
    
        if ct>2:
            return False
        return True
         
