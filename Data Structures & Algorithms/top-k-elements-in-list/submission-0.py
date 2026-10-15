class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = {}

        for _, val in enumerate(nums):
            h_map[val] = h_map.get(val, 0) + 1
        
        bucket = [ [] for _ in range(len(nums) + 1) ]

        for key, value in h_map.items():
            bucket[value].append(key)
        
        ret = []

        for bins in range(len(nums), 0, -1): 
            for elems in bucket[bins]:
                ret.append(elems)
                if len(ret) == k:
                    return ret