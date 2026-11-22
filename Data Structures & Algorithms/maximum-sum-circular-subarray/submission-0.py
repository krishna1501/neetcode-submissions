class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        
        maxSum = minSum = nums[0]
        curSum = 0
        curMin = 0
        for n in nums:
            curSum = max(curSum, 0) + n
            curMin = min(curMin, 0) + n
            maxSum = max(maxSum, curSum)
            minSum =min(minSum, curMin)
        if maxSum < 0:
            return maxSum
        return max(maxSum, totalSum - minSum) 

