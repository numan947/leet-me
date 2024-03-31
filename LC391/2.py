class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        totalDrink = 0
        emptyBottles = 0
        
        while numBottles>0:
            totalDrink += 1
            numBottles-=1
            emptyBottles+=1
            
            if emptyBottles>=numExchange:
                emptyBottles-=numExchange
                numBottles+=1
                numExchange+=1
        
        return totalDrink