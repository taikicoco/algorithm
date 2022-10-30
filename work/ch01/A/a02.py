from math import fabs


N, X = map(int,input().split())
A = list(map(int,input().split()))
Ans = False

for i in A:
    if X == i:
        Ans = True

if Ans:
    print("Yes")
else:
    print("No")
