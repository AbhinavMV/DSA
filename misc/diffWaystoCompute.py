class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        t = {}
        def compute(a,b,op):
            if(op=='+'):
                return a+b
            elif(op=='-'):
                return a-b
            else:
                return a*b
            
        def solve(exp):
            if(exp in t):
                return t[exp]
            if(exp.isdigit()):
                return [int(exp)]
            ans = []
            for i in range(len(exp)):
                if exp[i] in '+-*':
                    l = solve(exp[:i])
                    r = solve(exp[i+1:])
                    for x in l:
                        for y in r:
                            ans.append(compute(x,y,exp[i]))
            t[exp] = ans
            return ans
        
        return solve(expression)