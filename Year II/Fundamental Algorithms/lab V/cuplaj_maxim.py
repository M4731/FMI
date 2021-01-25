def lista_adiacenta(n,m,list,o):
    matx = [[]for i in range(n)] 

    if o == "neorientat":
        for i in list:
            matx[i[0]-1].append(i[1]-1)
            matx[i[1]-1].append(i[0]-1)
    elif o == "orientat":
        for i in list:
            matx[i[0]-1].append(i[1]-1)

    return matx


def cuplaj(list, n, l, r):
    cuplaje = 0
    ok = True
    while ok:
        ok = False
        v = []
        
        for i in range(n):
            if l[i] == -1 and path(i, v, list, r, l):
                cuplaje += 1
                ok = True
    return int(cuplaje/2)


def path(node, visited, list, r, l):
    if node in visited:
        return False
    visited.append(node)
    for i in list[node]:
        if r[i] == -1 or path(r[i], visited, list, r, l):
            l[node] = i
            r[i] = node
            return True
    return False



f = open("zgraf.in","r")
list = []
left = []
right = []
o = "neorientat"

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

for i in range(m):
    l = f.readline()
    list.append((int(l.split()[0]), int(l.split()[1])))
    if int(l.split()[0]) in left:
        if int(l.split()[1]) not in right:
            right.append(int(l.split()[1]))
    elif int(l.split()[0]) in right:
        if int(l.split()[1]) not in left:
            left.append(int(l.split()[1]))
    elif int(l.split()[1]) in right:
        if int(l.split()[0]) not in left:
            left.append(int(l.split()[0]))
    elif int(l.split()[1]) in left:
        if int(l.split()[0]) not in right:
            right.append(int(l.split()[0]))
    else:
        right.append(int(l.split()[1]))
        left.append(int(l.split()[0]))

l = [-1]*n
r = [-1]*n
lista = lista_adiacenta(n,m,list,o)

f.close()
ok = True
for i in left:
    for j in right:
        if i == j:
            ok = False

if ok == False:
    print("nu merge bro")
else:
    print(cuplaj(lista, n , l ,r))

    for i in range(0, n, 2):
        if l[i] != -1:
            print(i,l[i])