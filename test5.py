n = int(input())
x = []
for i in range(0, n):
    y = str(input())
    x.append(y)

for j in range(len(x)):
    t = x[j]
    for b in range(len(t)):
        if b%2==0:
            print(t[b], end='')
    print(' ', end='')
    for r in range(len(t)):
        if r%2!=0:
            print(t[r], end='')
    print("\n", end='')






