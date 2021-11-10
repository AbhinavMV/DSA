li = []
n = int(input())

for i in range(n):
    li.append(int(input()))

results = []
def solve(arr,n,k,ts,path):
    if(ts==0 and k==0):
        results.extend(path)
        return True
    if(n<0 or ts<0 or k<0):
        return False
    ans = False
    if(arr[n]<=ts):
        ans = solve(arr,n-1,k-1,ts-arr[n],path+[arr[n]])
    return ans or solve(arr,n-1,k,ts,path)
#print(li,sum(li))
for i in range(sum(li)//2,0,-1):
    if(solve(li,n-1,n//2,i,[])):
        temp = []
        for i in li:
            if i not in results:
                temp.append(i)
        print(results,temp)
        break
        