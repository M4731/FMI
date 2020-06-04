# Într-o zonă rezidențială se află o pădure foarte frumoasă, de forma unui dreptunghi. Un investitor
# isteț s-a gândit să-și construiască o vilă chiar în pădure, dar, fiind un ecologist convins, nu ar vrea
# să taie niciun copac. Din acest motiv, el ar vrea să afle zona dreptunghiulară din pădure cu
# suprafață maximă și în care nu este niciun copac. Investitorul are o hartă a întregii zone, în care
# sunt date coordonatele dreptunghiului corespunzător pădurii, precum și coordonatele tuturor
# copacilor din ea.
import math


def hasTree(x1, y1, x2, y2, v):
    for i in v:
        if (i[1]<y1 and i[1]>y2) and (i[0]<x1 and i[0]>x2):
            return i
    return False


def calcArie(x1, y1, x2, y2):
    return (x1 - x2) * (y1 - y2)

ariemare = 0
a = []


def divide(x1, y1, x2, y2, v):
    global ariemare
    global a
    if not hasTree(x1, y1, x2, y2, v):
        if calcArie(x1, y1, x2, y2) > ariemare:
            ariemare = calcArie(x1, y1, x2, y2)
            a = [x1, x2, y1, y2]
    else:
        i = hasTree(x1, y1, x2, y2, v)
        divide(x1, y1, x2, i[1], v)
        divide(x1, i[1], x2, y2, v)
        divide(i[0], y1, x2, y2, v)
        divide(x1, y1, i[0], y2, v)


f = open("copaci.in", "r")
g = open("copaci.out", "w")

v = []
x1 = 0
y1 = 0
x2 = math.inf
y2 = math.inf
for i in f.readlines():
    v.append(list(map(int, i.split())))
    y1, x1 = max(y1, v[-1][1]), max(x1, v[-1][0])
    y2, x2 = min(y2, v[-1][1]), min(x2, v[-1][0])
divide(x1, y1, x2, y2, v)
g.write("Dreptunghiul:"+'\n'+str(a[2])+" "+str(a[3])+'\n'+str(a[0])+" "+str(a[1])+'\n')
g.write("Aria maxima:"+'\n'+str(ariemare))