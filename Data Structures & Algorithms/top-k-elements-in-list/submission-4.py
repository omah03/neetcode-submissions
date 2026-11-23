from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        return sorted(num_count,key=num_count.get,reverse=True)[:k]
        