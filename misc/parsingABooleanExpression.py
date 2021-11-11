class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        def solve(exp,s,h):
            if(h-s==1):
                return exp[s]=='t'
            ans = exp[s]=='&'
            level, start = 0,s+2
            for i in range(s+2,h):
                if(level==0 and exp[i] in [',',')']):
                    cur = solve(exp,start,i)
                    start = i+1
                    if(exp[s]=='|'):
                        ans |= cur
                    elif(exp[s]=='&'):
                        ans &= cur
                    else:
                        ans = not cur
                if(exp[i]=='('):
                    level+=1
                if(exp[i]==')'):
                    level-=1
            return ans
        return solve(expression,0,len(expression))