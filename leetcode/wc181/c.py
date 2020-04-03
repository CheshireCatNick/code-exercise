from typing import List

to = [
    [0, 0]
    []
]
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def isIn(pos):
            if pos == (-1, 0) or pos == (0, -1): return True
            if pos[0] < 0 or pos[0] >= len(grid) or \
                    pos[1] < 0 or pos[1] >= len(grid[0]):
                return False
            return True
        def move(pos, d):
            if d == 'u':
                return (pos[0] - 1, pos[1])
            if d == 'd':
                return (pos[0] + 1, pos[1])
            if d == 'l':
                return (pos[0], pos[1] - 1)
            if d == 'r':
                return (pos[0], pos[1] + 1)

        def go(prev, now):
            print(prev, grid[i][j])
            if not isIn(prev) or not isIn(now):
                return (-1, -1)
            g = grid[now[0]][now[1]]
            d = ""
            if prev[0] == now[0]:
                if prev[1] > now[1]:
                    d = "l"
                else:
                    d = "r"
            else:
                if prev[0] > now[0]:
                    d = "u"
                else:
                    d = "d"
            if g == 1:
                if d == "r" or d == "l": return move(now, d)
                else: return (-1, -1)
            elif g == 2:
                if d == "u" or d == "d": return move(now, d)
                else: return (-1, -1)
            elif g == 3:
                if d == "u": return move(now, "l")
                elif d == "r": return move(now, "d")
                else: return (-1, -1)
            elif g == 4:
                if d == "u": return move(now, "r")
                elif d == "l": return move(now, "d")
                else: return (-1, -1)
            elif g == 5:
                if d == "d": return move(now, "l")
                elif d == "r": return move(now, "u")
                else: return (-1, -1)
            elif g == 6:
                if d == "d": return move(now, "r")
                elif d == "l": return move(now, "u")
                else: return (-1, -1)

        i = 0
        j = 0
        g = grid[0][0]
        if g == 1 or g == 
        while (canGo(i, j)):
            return True

s = Solution()
s.hasValidPath([[2,4,3],[6,5,2]])