class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        previous_sum = nums[0]
        result.append(nums[0])
        for i in range(1,len(nums)):
            previous_sum += nums[i]
            result.append(previous_sum)
        return result