class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        def solve(curr,path):
            if(curr==len(graph)-1):
                results.append(path)
            else:
                for i in graph[curr]:
                    solve(i,path+[i])
        results = []
        solve(0,[0])
        return results