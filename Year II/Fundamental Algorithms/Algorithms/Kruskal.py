def sortare(x):
    return int(x[2])


def init(x, tati, h):
    tati[x] = -1
    h[x] = 0


def find(x, tati):
    while tati[x] != -1:
        x = tati[x]
    return x


def union(x, y, tati, h):
    rx = find(x, tati)
    ry = find(y, tati)
    if h[rx] > h[ry]:
        tati[ry] = rx
    else:
        tati[rx] = ry
        if h[rx] == h[ry]:
            h[rx] += 1


f = open("zgrafpond.in","r")
list = []

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

l = f.readline()
while l:
    list.append((int(l.split()[0])-1, int(l.split()[1])-1, int(l.split()[2])))
    l = f.readline()

f.close()

tati = [-1]*n
h = [-1]*n
result = []

list.sort(key=sortare)

for i in range(n):
    init(i,tati, h)
nr = 0
for x in list:
    if find(x[0], tati) != find(x[1], tati):
        result.append(x)
        union(x[0],x[1],tati,h)
        nr += 1

        if nr == n-1:
            break

print(result)