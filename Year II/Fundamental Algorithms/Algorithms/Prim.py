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
            matx[i[0]-1].append(i[1]-1)

    return matx


def prim(list, start):
    result = []
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

resultat = prim(lista, 0)
print(resultat)