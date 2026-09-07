class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dict = {}

        for k,v in prerequisites:
            if pre_dict.get(k):
                pre_dict[k].append(v)
            else:
                pre_dict[k] = [v]

        visited = set()
        path_visited = set()

        def dfs(i):
            if i not in pre_dict or not pre_dict[i]:
                return True

            if i in visited and i in path_visited:
                return False

            visited.add(i)
            path_visited.add(i)

            preqs = pre_dict[i]
            for pre in preqs:
                if not dfs(pre):
                    return False

            path_visited.remove(i)
            return True      

        for course in range(numCourses):
            if not dfs(course):
                return False 

        return True 