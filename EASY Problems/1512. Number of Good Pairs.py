    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            a=i+1
            for j in range(a,n):
                if nums[i]==nums[j]:
                    cnt += 1
        return cnt
