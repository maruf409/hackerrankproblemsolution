n = int(input())
t = list(map(int, input().rstrip().split()))
t.reverse()
for i in range(n):
    j = t[i]
    print(j, '', end='')
