#aplicam algoritmul lui Dijkstra pentru fiecare nod sursa
#pe distantele obtinute pana in nodurile T calculam minimul
#mergem cu alt Dijkstra pentru a afla lantul

import sys
import queue

def lista_adiacenta(n,m,list,o):
    matx = [[]for i in range(n+1)] 

    if o == "neorientat":
        for i in list:
            matx[i[0]].append((i[1],i[2]))
            matx[i[1]].append((i[0],i[2]))
    elif o == "orientat":
        for i in list:
            matx[i[0]].append((i[1],i[2]))

    return matx


def dijkstra(list, start, T):
    n = len(list)-1
    distance = [sys.maxsize]*n
    distance[start] = 0
    v = []
    pqueue = queue.PriorityQueue()
    pqueue.put((0, start))

    while not pqueue.empty():
        node = pqueue.get()[1]
        if node not in v:
            v.append(node)
            for x in list[node]:
                next = x[0]
                cost = x[1]
                if distance[next] > distance[node] + cost:
                    distance[next] = distance[node] + cost
                    pqueue.put((distance[next],next))
    result = []
    for i in range(n):
        if i in T:
            result.append((i,distance[i]))
    return result


def dijkstra2(list, start, finish):
    n = len(list)-1
    tati = [-1]*n
    distance = [sys.maxsize]*n
    distance[start] = 0
    v = []
    pqueue = queue.PriorityQueue()
    pqueue.put((0, start))

    while not pqueue.empty():
        node = pqueue.get()[1]
        if node not in v:
            v.append(node)
            for x in list[node]:
                next = x[0]
                cost = x[1]
                if distance[next] > distance[node] + cost:
                    tati[next] = node
                    distance[next] = distance[node] + cost
                    pqueue.put((distance[next],next))

    index = finish
    rez = []
    while index != -1:
        rez.append(index)
        index = tati[index]
    return rez


f = open("graf.in","r")
list = []
T = []
start = []
o = "orientat"

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

for i in range(m):
    l = f.readline()
    list.append((int(l.split()[0])-1, int(l.split()[1])-1, int(l.split()[2])))

s = int(f.readline())
l = f.readline()
T=[int(i)-1 for i in l.split()]

for i in range(s):
    start.append(i) 

lista = lista_adiacenta(n,m,list,o)
f.close()

distances = {}
minim = sys.maxsize
sursa = -1
index = -1
for i in start:
    distances[i] = dijkstra(lista,i, T)

for i in distances.keys():
    for j in distances[i]:
        if minim > j[1]:
            minim = j[1]
            index = j[0]
            sursa = i
raspuns = dijkstra2(lista, sursa, index)

print("distanta intre multimi:"+str(minim))
print("s = "+str(sursa+1)+" t = "+str(index+1))

print("drum minim ",end="")
for i in range(len(raspuns)-1,-1,-1):
    print(str(raspuns[i]+1),end=" ")