"""
@author:Yuya
"""

n,sum = map(int,input().split())

K = list(map(int,input().split()))

S_set = set()

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                S_set.add(K[i]+K[j]+K[k]+K[l])


if sum in S_set:
    print("Yes")
else:
    print("No")