    def runningSum(self, nums: List[int]) -> List[int]:
        res = 0
        ans = []
        for i in nums:
            res = res + i
            ans.append(res)
        return ans
