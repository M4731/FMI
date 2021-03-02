import queue
import sys
#folosim prim cu toate distanlete = 1
#folosim dfs recursiv pt a creea alt arbore
#dist e distanta in al doilea arbore
#d e distanta in primul arbore


def lista_adiacenta(n,m,list,o):
    matx = [[]for i in range(n)] 

    if o == "neorientat":
        for i in list:
            matx[i[0]].append((i[1],1))
            matx[i[1]].append((i[0],1))
    elif o == "orientat":
        for i in list:
            matx[i[0]].append(i[1])

    return matx


def prim(list, start):
    result = []
    global d
    d[start] = 0
    pqueue = queue.PriorityQueue()
    v = []
    v.append(start)
    for i in list[start]:
        pqueue.put((i[1],(start,i[0])))
    
    while not pqueue.empty():
        bestcost = pqueue.get()
        cost = bestcost[0]
        next = bestcost[1][1]
        if next not in v:
            v.append(next)
            result.append((bestcost[1][0],bestcost[1][1],cost))

            for i in list[next]:
                pqueue.put((i[1],(next,i[0])))
                if d[next] >  d[i[0]] + 1:
                    d[next] = d[i[0]] + 1
    return result  


def  DFS(n, list):
    v = []
    result = []
    global dist
    dist[0] = 0

    for i in range(n):
        if i not in v:
            DFS3(i, v, list, result, dist)
    
    return result


def DFS3(n, v, list, result, dist):
    v.append(n)

    for i in list[n]:
        if i[0] not in v:
            result.append((n,i[0]))
            dist[i[0]] = min(dist[i[0]], dist[n]+1)
            DFS3(i[0], v, list, result, dist)


f = open("graf.in","r")
list = []
o = "neorientat"

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

for i in range(m):
    l = f.readline()
    list.append((int(l.split()[0])-1, int(l.split()[1])-1))

sursa = int(f.readline())-1

lista = lista_adiacenta(n,m,list,o)
f.close()

dist = [sys.maxsize]*n
d = [sys.maxsize]*n

x = prim(lista,sursa)
t1 = []
for i in x:
    t1.append((i[0],i[1]))

print("T1")
for i in t1:
    print(i[0]+1,i[1]+1)

t2 = DFS(n, lista)
print("T2")
for i in t2:
    print(i[0]+1,i[1]+1)


for i in range(len(d)):
    if d[i] != dist[i]:
        print("u = "+str(i+1))
        break


