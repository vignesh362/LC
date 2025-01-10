class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        k=''
        for i in range(len(num)):
            if num[i]=='6':
                k+='9'
                k+=num[i+1:]
                return int(k)
            else:
                k+=num[i]

        return int(k)

        