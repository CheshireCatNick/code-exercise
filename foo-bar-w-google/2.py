'''
Please Pass the Coded Messages
==============================

You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.
'''
'''
current complexity is O(2 ^ n)
a better solution can be achieved using dp where dp[i][j] = best ans with the first i numbers that % 3 == j
i = 1 ~ n
j = 0, 1, 2
ans = dp[n][0]
complexity: O(3n)
'''
def solution(l):
    n = len(l)
    ans = [0]
    for i in range(0, 2 ** n):
        s = []
        j = 0
        while i != 0:
            if i & 1:
                s.append(l[j])
            i >>= 1
            j += 1
        if sum(s) % 3 == 0:
            s.sort(reverse=True)
            if len(s) > len(ans) or (len(s) == len(ans) and s > ans):
                ans = s
    return int(''.join(list(map(str, ans))))

l = [3, 1, 4, 1, 5, 9]
print(solution(l))