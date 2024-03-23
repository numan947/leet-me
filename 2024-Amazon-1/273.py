class Solution:    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        lt20 = [
          '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]
        tens = [
             '', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]
        thousands = ['Billion', 'Million', 'Thousand', '']
        
        def convertLessThan1000(n):
            if n == 0:
                return ''
            elif n<20:
                return lt20[n]+' '
            elif n<100:
                return tens[int(n//10)] + ' '+convertLessThan1000(n%10)
            else:
                return lt20[int(n//100)]+ ' Hundred ' + convertLessThan1000(n%100)
        
        result = []
        div = 1e9
        idx = 0
        
        while div > 0:
            if num//div !=0:
                result.append(convertLessThan1000(num//div))
                result.append(thousands[idx])
                result.append(' ')
                num%=div
            idx+=1
            div//=1000
        return ''.join(result).strip()
s = Solution()
print(s.numberToWords(200))                 