class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        window_sum = curr_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k] 
            curr_sum = max(curr_sum, window_sum)

        curr_sum /= k
        return curr_sum