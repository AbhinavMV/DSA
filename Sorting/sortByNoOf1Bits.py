class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def noOf1s(num):
            a = num
            count=0
            while(a):
                a = a&(a-1)
                count+=1
            return count
        
        def compare(p,q):
            p1s = noOf1s(p)
            q1s = noOf1s(q)
            if(p1s!=q1s):
                return p1s<q1s
            else:
                return p<q
        
        def quickSort(array,left,right):
            if(left>right):
                return
            s = left
            e = right
            m = (s+e)//2
            pivot = array[m]
            while(s<=e):
                while(compare(array[s],pivot)):
                    s+=1
                while(compare(pivot,array[e])):
                    e-=1
                if(s<=e):
                    array[s],array[e] = array[e],array[s]
                    s+=1
                    e-=1
            quickSort(array,left,e)
            quickSort(array,s,right)
        #print(compare(3,8))   
        quickSort(arr,0,len(arr)-1)
        return arr
            
        