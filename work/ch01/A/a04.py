from traceback import print_tb


N = int(input())

Ans = ""
for i in range(9, 0-1, -1):
    if (N // 2**i) % 2 == 1:
        Ans += "1"
    else:
        Ans += "0"
print(Ans)
