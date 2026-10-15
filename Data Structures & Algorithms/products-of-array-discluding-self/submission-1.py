class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for idx in range(len(nums)):
            if idx == 0:
                prefix[idx] = nums[idx]
            else:
                prefix[idx] = nums[idx] * prefix[idx-1]

        for idx in range(len(nums)-1, -1, -1):
            if idx == len(nums)-1:
                suffix[idx] = nums[idx]
            else:
                suffix[idx] = nums[idx] * suffix[idx+1]
                
        for idx in range(len(nums)):
            if idx == 0:
                ret[idx] = suffix[idx+1]
            elif idx == len(nums)-1:
                ret[idx] = prefix[idx-1]
            else:
                ret[idx] = prefix[idx-1] * suffix[idx+1]
        return ret