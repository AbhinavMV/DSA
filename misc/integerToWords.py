class Solution:
    def numberToWords(self, num: int) -> str:
        
        self.lessThan20 = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        self.tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        self.hundreds = ['','Thousand','Million','Billion']
        
        if(num==0):
            return 'Zero'
    
        res = ''
        i = 0
        while(num>0):
            if(num%1000!=0):
                res = self.solve(num%1000) + self.hundreds[i] + ' ' + res
            num = int(num/1000)
            i+=1
        return res.strip()
    
    def solve(self,num):
        if(num==0):
            return ''
        if(num<20):
            return self.lessThan20[num] + ' '
        if(num<100):
            return self.tens[num//10] + ' ' + self.solve(num%10)
        else:
            return self.lessThan20[num//100] + ' Hundred ' + self.solve(num%100)