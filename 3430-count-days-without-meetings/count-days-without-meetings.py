class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        def isOverlap(p1,p2):
            # print(p1,p2)
            return max(p1[0], p2[0]) <= min(p1[1], p2[1])

        def combinedTime(p1,p2):
            p1.extend(p2)
            return [min(p1),max(p1)]
        meetings=sorted(meetings, key= lambda x:x[0])
        print(meetings)
        t=meetings[0]
        res=[]
        for i in range(1,len(meetings)):
            if isOverlap(t,meetings[i]):
                t=combinedTime(t,meetings[i])
            else:
                res.append(t)
                t=meetings[i]
        print(res)
        res.append(t)
        for i,j in res:
            days-=(j-i+1)
        return days

        