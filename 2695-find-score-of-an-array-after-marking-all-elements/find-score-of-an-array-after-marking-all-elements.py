import heapq
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        hqNum = [(num, i) for i, num in enumerate(nums)]  # Create min-heap directly
        heapq.heapify(hqNum)  # O(n) heapify instead of O(n log n) insertion
        marked = set()
        res = 0
        unmarked_count = len(nums)  # Track how many elements are still unmarked

        while unmarked_count > 0:
            j, i = heapq.heappop(hqNum)
            if i not in marked:
                res += j
                marked.add(i)
                unmarked_count -= 1  # Reduce unmarked count
                
                # Mark adjacent elements if not already marked
                if i - 1 >= 0 and i - 1 not in marked:
                    marked.add(i - 1)
                    unmarked_count -= 1
                if i + 1 < len(nums) and i + 1 not in marked:
                    marked.add(i + 1)
                    unmarked_count -= 1

        return res
