class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0,1
        curSum = nums[0]
        minLength = float("inf")

        while(right <= len(nums)):

            while(curSum >= target):
                minLength = min(right - left, minLength)
                curSum -= nums[left]

                left += 1

            if right == len(nums):
                break
            
            if curSum < target:
                curSum += nums[right]
                right += 1
                

        return 0 if minLength == float('inf') else minLength

