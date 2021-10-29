class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping =  {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        def solve(p,up):
            if(up==''):
                return [p]
            
            ch = up[0]
            li = []
            for i in mapping[ch]:
                li.extend(solve(p+i,up[1:]))
            return li
        
        ans = solve("",digits)
        return [] if ans==[""] else ans
        