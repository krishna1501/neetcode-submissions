class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        numsSum = 0
        count = 0
        for i in range(k):
            numsSum += nums[i]
            print(numsSum)
        
        if numsSum//k >= threshold:
                count += 1

        for i in range(k,len(nums)):
            numsSum += nums[i]
            numsSum -= nums[i-k]
            if numsSum//k >= threshold:
                count += 1
            
        return count
                

            