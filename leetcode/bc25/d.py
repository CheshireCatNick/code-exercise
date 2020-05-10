class Solution:
    def numberWays(self, hats) -> int:
        # state => count
        states = {}
        for hat in hats[0]:
            state = [0] * 9
            state[hat - 1] = 1
            states[tuple(state)] = 1
        for i in range(1, len(hats)):
            nStates = {}
            hs = hats[i]
            for state in states:
                count = 0
                for hat in hs:
                    if state[hat - 1] == 0:
                        nState = list(state)
                        nState[hat - 1] = 1
                        nState = tuple(nState)
                        if nState in nStates:
                            nStates[nState] += states[state]
                        else:
                            nStates[nState] = states[state]
            states = nStates
        ans = 0
        for state in states:
            ans += states[state]
        return ans

s = Solution()
s.numberWays([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
