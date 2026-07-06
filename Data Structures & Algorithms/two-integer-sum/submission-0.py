class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    # [3,4,5,6] target = 7 return [0,1] (smallest index first)

        my_map = {}

        for idx, v in enumerate(nums):
            diff = target - v # 7 - 4 ; diff = 3

            if diff in my_map:
                return [my_map[diff], idx]
        
            else:               # v : idx
                my_map[v] = idx # 3 : 0
