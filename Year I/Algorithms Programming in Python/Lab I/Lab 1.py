import math
"""
1. Pentru ecuația de gradul doi aa ∗ xx2 + bb ∗ xx + cc = 0, să se citească de la
tastatură coeficienții a, b, c (numere întregi). Știind formulele dd(dddddddddd) =
bb2 − 4 ∗ aa ∗ cc și xx1,2 = −bb±√dd

2∗aa , să se afișeze dacă ecuația nu are nicio rădăcină
(pentru dd < 0), are o singura rădăcină xx = ⋯ (pentru dd = 0), sau are două
rădăcini distincte xx1 = ⋯ și xx2 = ⋯ (pentru dd > 0).


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = int(b**2 - 4*a*c)
if d < 0:
    print("nu exista radacina.")
elif d == 0:
    print("radacina este ")
    q = float((-b)/(2*a))
    print(q)
else:
    print("imi e lene da am inteles ideea ")
"""

"""
2. Un meșter trebuie să paveze întreaga pardoseală a unei bucătării cu formă
dreptunghiulară de dimensiune LL1 × LL2 centimetri, cu plăci de gresie pătrate,
toate cu aceeași dimensiune. Știind că meșterul nu vrea să taie nici o placă de
gresie și vrea să folosească un număr minim de plăci, să se determine
dimensiunea plăcilor de gresie de care are nevoie, precum și numărul lor. De
exemplu, dacă LL1 = 440 cm și LL2 = 280 cm, atunci meșterul are nevoie de
77 de plăci de gresie, fiecare având latura de 40 cm.

def cmmdc ( a , b ) :
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


L1 = int(input("lungime = "))
L2 = int(input("latime = "))
a = L1 * L2
s = cmmdc(L1, L2)
LP = int(a/s**2)
print("este nevoie de ", LP, " placi de gresie, fiecare avand latura de ", s," cm")
"""

"""
3. Un greiere se deplasează efectuând câte o săritură, lungimea inițială a
săriturii fiind de xx cm. După fiecare nn sărituri, lungimea săriturii greierului se
micșorează cu pp procente. Cunoscându-se valorile xx, nn, pp, precum și
numărul de sărituri mm pe care le face greierele, să se scrie un program care să
afișeze distanța parcursă de greiere. De exemplu, pentru xx = 20, nn =
10, pp = 10 și mm = 20 distanța parcursă de greiere este egală cu 380 cm,
deoarece primele 10 sărituri efectuate au, fiecare, lungimea de 20 cm, iar
următoarele 10 au, fiecare, lungimea de 18 cm.

x = int(input("x = "))
n = int(input("n = "))
cop = n
p = int(input("p = "))
m = int(input("m = "))
dist = 0
while m:
    if n == 0:
        n = cop
        x -= (p/100)*x
    dist += x
    n -= 1
    m -= 1

print("Greierele a parcurs ", dist, " cm.")
"""

"""
4. Se citește un șir format din nn numere reale strict pozitive (nn ≥ 2),
reprezentând cursul de schimb valutar RON/EURO din nn zile consecutive. Să
se afișeze zilele între care a avut loc cea mai mare creștere a cursului valutar,
precum și cuantumul acesteia. De exemplu, pentru nn = 6 zile și cursul valutar
dat de șirul 4.25, 4.05, 4.25, 4.48, 4.30, 4.40, cea mai mare creștere a fost de
0.23 RON, între zilele 3 și 4.

max = 0
l = []
n = int(input("nr zile: "))
for i in range(n):
    x = float(input())
    l.append(x)
for i in range(len(l)-1):
    if l[i] - l[i-1] > max:
        max = l[i] - l[i-1]
        w = i
        ww = i-1
max = str(round(max, 2))  #rotunjirea la 2 zecimale
print("cea mai mare creștere a fost de", max, "RON, intre zilele ", ww, "si", w ,".")
"""

"""
5. Se citește un șir format din nn numere întregi (nn ≥ 2). Să se afișeze cele mai
mari două valori distincte din șir sau mesajul "Imposibil", dacă acestea nu
există.

nn = int(input("nr: "))
max1 = 0
max2 = 0
myl = []
for i in range(nn):
    x = int(input())
    if x > max1:
        max1 = x
    myl.append(x)
for i in range(len(myl)-1):
    if myl[i] > max2 and myl[i] != max1:
        max2 = myl[i]
print("maximurile :",max1,max2)
"""

"""
6. Se citește un număr natural nenul nn. Să se afișeze cel mai mic și cel mare
număr ce pot fi formate din cifrele lui nn. De exemplu, pentru nn = 812383
trebuie afișate numerele 883321 și 123388.
"""
n = int(input("numarul: "))
myl = []
while n:
    myl.append(n % 10)
    n //= 10

cyl = myl.copy()
nr = 0
while cyl:
    max = 9223372036854775807
    for x in cyl:
        if x < max :
            max = x
    if nr == 0:
        max2 = 9223372036854775807
        for x in cyl:
            if x < max2 and x != max:
                max2 = x
    if nr == 0 and max == 0:
        nr = nr * 10 + max2
        cyl.remove(max2)
    else:
        nr = nr * 10 + max
        cyl.remove(max)
print("minimul posibil:",nr)

cy = myl.copy()
nrr = 0
while cy:
    min = 0
    for x in cy:
        if x > min:
            min = x
    nrr = nrr*10 + min
    cy.remove(min)
print("maximul posibil:", nrr)

