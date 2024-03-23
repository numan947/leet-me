class Solution:
    def intToRoman(self, num: int) -> str:
        # ans = ''
        
        # while num>0:
        #     if num >=1000:
        #         ans += 'M'*(num//1000)
        #         num%=1000
            
        #     if num >=900:
        #         ans += 'CM'
        #         num%=900
            
        #     if num >= 500:
        #         ans += 'D'*(num//500)
        #         num%=500
            
        #     if num>=400:
        #         ans += 'CD'
        #         num%=400
            
        #     if num>= 100:
        #         ans += 'C'*(num//100)
        #         num%=100
            
        #     if num>=90:
        #         ans += 'XC'
        #         num%=90
            
        #     if num >=50:
        #         ans += 'L'*(num//50)
        #         num%=50
            
        #     if num >=40:
        #         ans += 'XL'
        #         num%=40
              
        #     if num >=10:
        #         ans += 'X'*(num//10)
        #         num%=10
            
        #     if num >=9:
        #         ans += 'IX'*(num//9)
        #         num%=9
            
        #     if num>=5:
        #         ans += 'V'*(num//5)
        #         num%=5
        #     if num>=4:
        #         ans += 'IV'
        #         num%=4
        #     if num<=3:
        #         ans += 'I'*num
        #         num = 0
        
        # return ans
        
        
        ans = ''
        
        symList = [
			["I", 1],
			["IV",4],
			["V", 5],
			["IX", 9],
			["X", 10],
			["XL", 40],
			["L", 50],
			["XC", 90],
			["C", 100],
			["CD", 400],
			["D", 500],
			["CM", 900],
			["M", 1000]
		]
        
        for sym, val in reversed(symList):
            if num//val:
                ans += (sym*(num//val))
                num%=val
        return ans
    
s = Solution()
print(s.intToRoman(1994))