import sys

f = open("graph.in","r")
l = f.readline()
linii = int(l.split()[0])
coloane = int(l.split()[1])

matrix = [[]for i in range(linii)]
index = []

for i in range(linii):
    l = f.readline().split()
    for j in range(len(l)):
        matrix[i].append(int(l[j]))
        if int(l[j]) == 1:
            index.append((i,j))

list = []   
l = f.readline()
while l:
    list.append((int(l.split()[0])-1, int(l.split()[1])-1))
    l = f.readline()

f.close()
f = open("graph.out","w")

for i in list:
    minim = sys.maxsize
    tup = (0,0)
    for j in index:
        x = abs(j[0]-i[0]) + abs(j[1]-i[1])
        if x < minim:
            minim = x
            tup = j
    f.write(str(minim)+" ["+str(tup[0]+1)+", "+str(tup[1]+1)+"]\n")


# print(index)
# print(list)
# print(*matrix,sep="\n")