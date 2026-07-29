class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        maxi = 0

        for num in nums:
            if num == 1:
                curr += 1
                maxi = max(maxi, curr)
            else:
                curr = 0

        return maxi