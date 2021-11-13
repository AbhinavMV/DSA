class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factor = 1
        arr = []
        for i in range(1,n+1):
            arr.append(i)
            factor*=i
        index = 0
        res = []
        k -= 1 
        factor /= n
        
        for m in range(n-1,0,-1):
            index = int(k//factor)
            res+=str(arr[index])
            arr.pop(index)
            k %= factor
            factor /= m
        res += str(arr[0])
        return ''.join(res)
        
        
        # arr = [i for i in range(1,n+1)]
        # self.count = k
        # def solve(arr,l,path):
        #     if(self.count==0):
        #         return
        #     if(l==0):
        #         self.count-=1
        #         if(self.count==0):
        #             self.results = path
        #             return
        #     else:
        #         for i in range(len(arr)):
        #             solve(arr[:i]+arr[i+1:],l-1,path+[str(arr[i])])
        # self.results = ''
        # solve(arr,n,[])
        # return ''.join(self.results)