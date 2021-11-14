class Solution:
    def calculate(self, s: str) -> int:
        def compute(sign,num,stack):
            if(sign=='+'):
                stack.append(num)
            elif(sign=='-'):
                stack.append(-num)
        
                
        def solve(exp,pos):

            num,stack,i,sign = 0,[],pos,'+'
            while(i<len(exp)):
                if(exp[i].isdigit()):
                    num = num*10 + int(exp[i])
                elif(exp[i] in '+-'):
                    compute(sign,num,stack)
                    sign = exp[i]
                    num = 0
                elif(exp[i]=='('):
                    num,j = solve(exp,i+1)
                    i = j
                elif(exp[i]==')'):
                    compute(sign,num,stack)
                    return sum(stack),i
                i+=1
            compute(sign,num,stack)
            return sum(stack),i
        ans = solve(s,0)
        return ans[0]