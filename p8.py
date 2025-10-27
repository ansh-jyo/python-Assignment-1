t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if b == 0:
        print(1)
        continue
    a %= 10
    p = [pow(a, i, 10) for i in range(1, 5)]
    print(p[b % 4 - 1])
