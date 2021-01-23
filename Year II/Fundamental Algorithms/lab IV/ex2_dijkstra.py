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


def dijkstra(list, control, start):
    n = len(list)
    distance = [sys.maxsize]*n
    distance[start] = 0
    v = []
    tati = [-1]*n
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
    result = []
    for i in range(n):
        result.append((i,distance[i]))

    maindist = sys.maxsize
    index = -1
    for i in result:
        if i[0] in control:
            if i[1] < maindist:
                maindist = i[1]
                index = i[0]
    ind = index
    rez = []
    while index != -1:
        rez.append(index)
        index = tati[index]

    return((distance[ind],rez))



f = open("control.txt","r")
list = []

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

for i in range(m):
    l = f.readline()
    list.append((int(l.split()[0])-1, int(l.split()[1])-1, int(l.split()[2])))

control = []
l = f.readline()
for i in l.split():
    control.append(int(i)-1)

f.close()
lista = lista_adiacenta(n,m,list,"neorientat")
print(control)
print(lista)
print(dijkstra(lista,control,0))