"""
3. Scrieți un program care să înlocuiască într-o propoziție toate aparițiile unui cuvânt ss cu un cuvânt
tt. Atenție, NU se poate utiliza metoda replace! De ce?
"""
s = str(input("text: "))
x = str(input("cuvant de inlocuit: "))
y = str(input("cuvant cu care se inlocuieste: "))
s2 = ""
s = s.split()
for i in s:
    if i == x:
        s2 += y+" "
    else:
        s2 += i+" "
print("sir final:",s2)

