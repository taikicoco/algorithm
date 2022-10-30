A, B = map(int,input().split())
Ans = False
for i in range(A, B+1, 1):
    if 100 % i == 0:
        Ans = True

if Ans:
    print("Yes")
else:
    print("No")
    