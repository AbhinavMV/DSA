class Solution:
    def decodeString(self, s: str) -> str:
        def solve(s,pos):
            res = ''
            num,i = 0,pos
            while(i<len(s)):
                if(s[i].isdigit()):
                    num = num*10 + int(s[i])
                elif(s[i]=='['):
                    local,temp_pos = solve(s,i+1)
                    i = temp_pos
                    res += local*num
                    num = 0
                elif(s[i]==']'):
                    return res,i
                else:
                    res+= s[i]
                i+=1
            return res,i
        
        return solve(s,0)[0]
        