from typing import List

INF: int = 100000000
n: int # Payment Amount
m: int # Number of coins
n, m = map(int, input().split())
c: List[int] = list(map(int, input().split()))

T: List[int] = [INF for j in range(n + 1)]

for i in range(1, m + 1):
    j: int = 0
    while j + c[i] <= n:
       T[j + c[i]] = min(T[j + c[i]], T[j] + 1)
       j += 1

print("Result:{0}".format(T[n]))