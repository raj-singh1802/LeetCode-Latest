class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            curr_sum = 0
            temp = num
            while temp > 0:
                curr_sum += temp % 10
                temp //= 10
            if curr_sum == i:
                return i
        return -1