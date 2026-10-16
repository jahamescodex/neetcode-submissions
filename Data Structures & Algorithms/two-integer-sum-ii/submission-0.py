class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            val = numbers[r] + numbers[l] 
            
            if val > target:
                r -= 1
                continue

            if val < target:
                l += 1
                continue
            if target == val:
                break

        return [l+1,r+1]
