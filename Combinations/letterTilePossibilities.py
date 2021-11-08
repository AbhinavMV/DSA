class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        li = [i for i in tiles]
        li.sort()
        a = ''.join(li)
        results = []
        def solve(string,path):
            results.append(path)
            for i in range(len(string)):
                if(i>0 and string[i]==string[i-1]):
                    continue
                path.append(string[i])
                solve(string[:i]+string[i+1:],path[:])
                path.pop()
        cur = []
        solve(a,cur)
        return len(results)-1