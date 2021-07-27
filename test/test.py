def append(t, a):
    if t is None:
        return (a,)
    return tuple([a] + list(t))
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        classes = [None] * numCourses
        for r in prerequisites:
            print(r[0], r[1])
            if not classes[r[0]]:
                classes[r[0]] = type(str(r[0]), (), {})
            if not classes[r[1]]:
                classes[r[1]] = type(str(r[1]), (classes[r[0]],), {})
            else:
                classes[r[1]] = type(str(r[1]), append(classes[r[1]].__bases__, classes[r[0]]), {})
        for c in classes:
            print(c.mro())

s = Solution()
s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])