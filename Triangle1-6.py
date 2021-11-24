"""
@author:Yuya
"""
n = int(input())
a = sorted(list(map(int,input().split())))

ans = list()  #ans : 答え

#i < j < k(重複しないように区別する必要がある)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            length = a[i] + a[j] + a[k]  #length : 周長
            if ((a[i] + a[j]) - a[k]) > 0:
                ans.append(length)

if len(ans) > 0:
    print(max(ans))
else:
    print(0)