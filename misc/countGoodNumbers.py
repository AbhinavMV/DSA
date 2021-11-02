class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def power(x,y,mod):
            if(y==0):
                return 1
            temp = power(x,y//2,mod)
            if(y%2==0):
                return (temp*temp)%mod
            else:
                return (temp*temp*x)%mod
        p5=0
        p4=n//2
        if(n%2==0):
            p5=n//2
        else:
            p5=n//2+1
        mod=10**9+7
        return (power(5,p5,mod)*power(4,p4,mod))%mod
        
        # if(n%2==0):
        #     return (5**(n//2)*4**(n//2))%(10**9+7)
        # else:
        #     return (5**(n//2+1)*4**(n//2))%(10**9+7)
        
        
#         if(n==1):
#             return 5
        
#         upper = '9'*n
#         lower = '9'
#         count = 0
        
#         while(int(upper)>int(lower)):
#             upper = ((n-len(upper)) * '0') + upper
            
#             for i in range(n):
#                 if(i%2==0 and int(upper[i])%2!=0):
#                     break
#                 elif(i%2!=0 and upper[i] not in ['2','3','5','7']):
#                     break
#             else:
#                 count+=1
#             upper = str(int(upper)-1)
            
#         return count%(10**9 + 7)