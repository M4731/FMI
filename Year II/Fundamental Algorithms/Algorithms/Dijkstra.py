import sys
import queue

def lista_adiacenta(n,m,list,o):
    matx = [[]for i in range(n)] 

    if o == "neorientat":
        for i in list:
            matx[i[0]].append((i[1],i[2]))
            matx[i[1]].append((i[0],i[2]))
    elif o == "orientat":
        for i in list:
            matx[i[0]].append((i[1],i[2]))

    return matx


def dijkstra(list, start):
    n = len(list)
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
        result.append((i,distance[i]))
    return result



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
lista = lista_adiacenta(n,m,list,"neorientat")

print(dijkstra(lista,0))