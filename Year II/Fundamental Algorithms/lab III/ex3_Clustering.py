import sys

def levenshtein(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(levenshtein(a[1:], b[1:])+(a[0] != b[0]),
               levenshtein(a[1:], b)+1,
               levenshtein(a, b[1:])+1)


def find(x, dict):
    for i in dict.keys():
        if x in dict[i]:
            return i


def union(x,y,dictionar):
    dictionar[x].extend(dictionar[y])
    if len(dictionar[y]) != 0:
        dictionar.pop(y)


k=3

f = open("cuvinte.in","r")
list = []
y = []

l = f.readline()
while l:
    list.extend(l.split())
    l = f.readline()

for i in list:
    for j in list:
        if i != j:
            y.append((i,j,levenshtein(i, j)))

dictionar = {}

for i in list:
    dictionar[i] = [i]    


y.sort(key=lambda x: x[2])

for x in y:
    if find(x[0], dictionar) != find(x[1], dictionar):
        union(x[0],x[1],dictionar)
    if len(dictionar.keys()) == k:
        break

print(dictionar)

minim = sys.maxsize

for x in dictionar.keys():
    for y in dictionar.keys():
        if x != y:
            for i in dictionar[x]:
                for j in dictionar[y]:
                    if minim > levenshtein(i,j):
                        minim = levenshtein(i,j)

print(minim)
f.close()