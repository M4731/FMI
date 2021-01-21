def matrice_adiacenta(n, m, list, o):
    mat = [[0]*n for i in range(n)]

    if o == "neorientat":
        for i in list:
            #print(i[0], i[1])
            a1 = i[0] -1
            a2 = i[1] -1
            mat[a1][a2] = mat[a2][a1] = 1   
    elif o == "orientat":
        for i in list:
            a1 = i[0] -1
            a2 = i[1] -1
            mat[a1][a2] =  1

    return mat

def afisare_matrice(matrix):
    print(*matrix,sep="\n")


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

def afisare_lista(matrix):
    print(*matrix,sep="\n")

def matrice_la_lista(matrix):
    matx = [[]for i in range(n)] 

    for i in range (len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                matx[i].append(j)

    return matx

def lista_la_matrice(matx):
    mat = [[0]*n for i in range(n)]

    for i in range(len(matx)):
        #print(matx[i])
        for j in matx[i]:
            mat[i][j] = 1

    #print(*mat,sep="\n")
    return mat
        

f = open("graf.in","r")
list = []

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

l = f.readline()
while l:
    list.append((int(l.split()[0]), int(l.split()[1])))
    l = f.readline()

# print(n,end=" ")
# print(m)
# print(list)

o = "neorientat"
mat_ad = matrice_adiacenta(n,m,list,o)
#afisare_matrice(m)
list_ad = lista_adiacenta(n,m,list,o)
#afisare_lista(list_ad)
list_ad2 = matrice_la_lista(mat_ad)
mat_ad2 = lista_la_matrice(list_ad)

f.close()