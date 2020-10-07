# 7. Se dau doi vectori a și b de lungime n, respectiv m, cu elementele ordonate crescător. Propuneți un
# algoritm cât mai eficient pentru a determina mediana vectorului obținut prin interclasarea celor
# doi vectori O(log(min{n,m}))


def getMedian(v):
    if len(v) % 2 == 0:
        return (v[(len(v)//2)-1] + v[len(v)//2]) / 2
    else:
        return v[(len(v)-1) // 2]


def divide(v, w):
    if len(v) <= 2:
        qw = [w[len(w)//2-1], w[len(w)//2], w[len(w)//2+1]]
        s = []
        for i in v:
            s.append(i)
        for i in qw:
            s.append(i)
        s.sort()
        return int(getMedian(s))
    else:
        x = getMedian(v)
        y = getMedian(w)
        if x == y:
            return(x)
        elif x < y:
            v = v[0:len(v)//2+1]
            w = w[len(v)//2:len(w)+1]
        else:
            v = v[len(v)//2:len(v)]
            w = w[0:len(w)-(len(v)//2+1)+1]
    return divide(v, w)


f = open("date.in", "r")
n = int(f.readline())
w = []
v = (f.readline().split())
m = int(f.readline())
s = f.readline().split()
for i in range(n):
    w.append(int(v[i]))
v.clear()
for i in range(m):
    v.append(int(s[i]))
s.clear()
print(divide(v, w))
