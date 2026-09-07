class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dict = {}

        for k,v in prerequisites:
            if pre_dict.get(k):
                pre_dict[k].append(v)
            else:
                pre_dict[k] = [v]

        visited = set()
        
        def dfs(i):
            if i not in pre_dict or not pre_dict[i]:
                return True

            if i in visited:
                return False

            visited.add(i)

            preqs = pre_dict[i]
            for pre in preqs:
                if not dfs(pre):
                    return False

            visited.remove(i)
            pre_dict[i] = []
            
            return True      

        for preq in prerequisites:
            if not dfs(preq[0]):
                return False 

        return True 