    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >=a :
                candies[i]=True
            else:
                candies[i]=False
        return candies
        
