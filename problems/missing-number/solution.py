class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = (n * (n+1)) // 2
        actualSum = sum(nums)

        missingNum = expectedSum - actualSum
        return missingNum
        
        # This is also one of the solution using XOR operations
        # result = n
        # for i in range(n):
        #     result ^= i
        #     result ^= nums[i]
        # return result