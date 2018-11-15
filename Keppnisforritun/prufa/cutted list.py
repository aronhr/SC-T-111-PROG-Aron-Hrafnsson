k = int(input())
t = k//3
z = t+t
i = input().split()
h = [int(b) for b in i]
p = sorted(h)
f = p[:t]
m = p[t:z]
l = p[z:]

merged = m+f+l
print(*merged)