class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        curr_max = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= curr_max:
                res.append(True)
            else: res.append(False)
        return res