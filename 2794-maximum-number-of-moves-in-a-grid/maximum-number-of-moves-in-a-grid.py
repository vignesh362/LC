class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # bg=float('-inf')
        t=[[-1,1],[0,1],[1,1]]
        memo={}
        def moveBig(x,y,mv):
            mxMv=0
            if (x,y) in memo:
                return memo[(x,y)]
            for i,j in t:
                mx,my=i+x,j+y
                if 0<=mx<len(grid) and 0<=my<len(grid[0]) and grid[mx][my]>grid[x][y]:
                    mxMv=max(mxMv,1+moveBig(mx,my,mv+1))
            memo[(x,y)]=mxMv
            return mxMv



        res=0
        for k in range(len(grid)):
            res=max(res,moveBig(k,0,0))
        return res
                


        