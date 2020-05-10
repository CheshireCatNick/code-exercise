from collections import deque
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ind = {}
        for c in "croak":
            ind[c] = []
        for i in range(len(croakOfFrogs)):
            c = croakOfFrogs[i]
            if not c in ind:
                return -1
            ind[c].append(i)
        for c in ind:
            if not len(ind[c]) == len(ind["c"]):
                return -1
        for i in range(len(ind["c"])):
            prevInd = -1
            for c in ind:
                if ind[c][i] - prevInd < 0:
                    return -1
                prevInd = ind[c][i]
        queue = deque()
        count = 0
        for i in range(len(ind["c"])):
            s = ind["c"][i]
            e = ind["k"][i]
            while len(queue) > 0 and queue[0] < s:
                queue.popleft()
            queue.append(e)
            count = max(count, len(queue))
        return count

s = Solution()
print(s.minNumberOfFrogs("croakcroak"))