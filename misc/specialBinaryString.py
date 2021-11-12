class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        
        def solve(exp):
            balance = start = 0
            ans = []
            for i in range(len(exp)):
                if(exp[i]=='1'):
                    balance+=1
                else:
                    balance-=1
                if(balance==0):
                    ans.append('1'+solve(exp[start+1:i])+'0')
                    start=i+1
            return ''.join(sorted(ans)[::-1])
        return solve(s)