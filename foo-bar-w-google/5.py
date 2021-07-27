'''
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.
'''
from collections import deque
def solution(map_):
    m = len(map_)
    n = len(map_[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * n for i in range(m)]
    q = deque([(m - 1, n - 1, 1)])
    visited[m - 1][n - 1] = True
    # minimum distance from i, j to the exit if cannot change any wall
    md = [[-1] * n for i in range(m)]
    while len(q) > 0:
        x, y, dist = q.popleft()
        md[x][y] = dist
        for d in dirs:
            n_x, n_y = x + d[0], y + d[1]
            if 0 <= n_x and n_x < m and 0 <= n_y and n_y < n and not map_[n_x][n_y] and not visited[n_x][n_y]:
                visited[n_x][n_y] = True
                q.append((n_x, n_y, dist + 1))
    #print(md)
    visited = [[False] * n for i in range(m)]
    q = deque([(0, 0, 1)])
    visited[0][0] = True
    ans = m * n
    while len(q) > 0:
        x, y, dist = q.popleft()
        #print(f'this is {x} {y} {dist}')
        for d in dirs:
            n_x, n_y = x + d[0], y + d[1]
            if 0 <= n_x and n_x < m and 0 <= n_y and n_y < n:
                if md[n_x][n_y] != -1:
                    #print(f'calc {n_x} {n_y}')
                    ans = min(ans, dist + md[n_x][n_y])
                else:
                    #print(f'trying around wall {n_x} {n_y}')
                    for d in dirs:
                        nn_x, nn_y = n_x + d[0], n_y + d[1]
                        if 0 <= nn_x and nn_x < m and 0 <= nn_y and nn_y < n and md[nn_x][nn_y] != -1:
                            ans = min(ans, dist + 1 + md[nn_x][nn_y])
                #print(f'ans = {ans}')
                if not visited[n_x][n_y] and not map_[n_x][n_y]:
                    #print(f'adding {n_x} {n_y}')
                    q.append((n_x, n_y, dist + 1))
                visited[n_x][n_y] = True
    return ans

#m = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
m = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

print(solution(m))