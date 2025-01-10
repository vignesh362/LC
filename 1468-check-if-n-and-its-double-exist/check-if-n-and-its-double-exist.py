class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visited=set()

        for i in arr:
            if i*2 in visited or (i//2 in visited and i//2*2==i):
                return True
            visited.add(i)
        return False
        