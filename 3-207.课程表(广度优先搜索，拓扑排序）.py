#time 41.03 room 35.00
def canFinish(numCourses, prerequistes):
    indegrees = [0 for i in range(numCourses)]
    if prerequistes == []:
        return True
    queue, dicts = [], {}
    for item in prerequistes:
        indegrees[item[0]] += 1
        dicts.setdefault(item[1], [])
        dicts[item[1]].append(item[0])
    for i in range(numCourses):
        if indegrees[i] == 0:
            queue.append(i)
    while queue != []:
        pop = queue[0]
        queue = queue[1:]
        for i in dicts[pop]:
            indegrees[i] -= 1
            if indegrees[i] == 0:
                queue.append(i)
    for i in range(numCourses):
        if indegrees[i] != 0:
            return False
    return True
