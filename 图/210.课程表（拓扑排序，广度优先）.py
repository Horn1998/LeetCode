#time 90 room 31
class Solution:
    def findOrder(self, numCourses: int, prerequistes):
        indegrees = [0 for i in range(numCourses)]
        ans = []
        if prerequistes == []:
            for i in range(numCourses):
                ans.append(i)
            return ans
        queue, dicts = [], {}
        for i in range(numCourses):
            dicts[i] = []
        for item in prerequistes:
            indegrees[item[0]] += 1
            dicts[item[1]].append(item[0])
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        while queue != []:
            pop = queue[0]
            ans.append(pop)
            queue = queue[1:]
            for i in dicts[pop]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        for i in range(numCourses):
            if indegrees[i] != 0:
                return []
        return ans