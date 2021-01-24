import sys

def topological_sorting(list):
    v = []
    result = []

    for i in range(len(list)):
        if i not in v:
            DFS(i,list,v,result)
        
    return(result[::-1])

def DFS(start, list, visited, result):
    visited.append(start)

    for i in list[start]:
        if i[0] not in visited:
            DFS(i[0],list,visited,result)

    result.append(start)


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


def DAG(start, list):
    n = len(list)
    distance = [sys.maxsize]*n
    tati = [-1]*n
    distance[start] = 0  

    sort_top = topological_sorting(list)  
    for x in sort_top:
        for i in list[x]:
            if distance[x] + i[1] < distance[i[0]]:
                distance[i[0]] = distance[x] + i[1]
                tati[i[0]] = x
    result = []
    for i in sort_top:
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

lista = lista_adiacenta(n,m,list,"orientat")

print(DAG(0,lista))
f.close()   