from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates)
        counter = [(key,counter[key]) for key in counter]
        results = []
        size = len(counter)
        print(counter)
        def solve(curr,path,t):
            if(t<0 or curr>=size):
                return
            elif(t==0):
                results.append(path)
            else:
                candidate,freq = counter[curr]
                if(freq>0):
                    counter[curr] = (candidate,freq-1)
                    solve(curr,path+[candidate],t-candidate)
                counter[curr] = (candidate,freq)
                solve(curr+1,path,t)

        solve(0,[],target)
        return results