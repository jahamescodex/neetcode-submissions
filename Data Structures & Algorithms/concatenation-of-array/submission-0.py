class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ret = [0] * (2*length)

        for idx in range(len(ret)):
            if idx >= length:
                ret[idx] = nums[idx-length]
            else:
                ret[idx] = nums[idx]
        return ret