    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in accounts:
            wealth = sum(i)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
