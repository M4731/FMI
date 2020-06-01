# 1. Minimizarea timpului mediu de așteptare
# Din fișierul “tis.txt” se citesc numere naturale nenule reprezentând timpii necesari pentru servirea
# fiecărei persoane care așteaptă la o coadă.
# Să se determine ordinea în care ar trebui servite persoanele de la coadă astfel încât timpul mediu
# de așteptare să fie minim.
# Indicație de rezolvare:
# - Se creează o listă de tupluri care să conțină, pentru fiecare persoană, numărul său de ordine în
# lista inițială și timpul individual de servire pentru acea persoană.
# - Se definește o funcție “afisare_timpi_servire (tis)” care primește ca parametru o listă de tupluri
# de tipul indicat mai sus și afișează pentru fiecare persoană, pe 3 coloane, următoarele
# informații: numărul de ordine al persoanei, timpul individual de servire și timpul său de
# așteptare. La final se afișează timpul mediu de așteptare al tuturor persoanelor.
# - Se apelează funcția de mai sus pentru lista inițială, iar apoi pentru lista care a fost sortată
# crescător după timpul individual de servire.
# Exemplu: Dacă “tis.txt” conține numerele 7 15 3 7 8 3 2 10 5 4 2,
# atunci timpul mediu de așteptare inițial va fi: 41.73
# iar timpul mediu de așteptare după sortarea listei va fi: 24.82

f = open("tis.txt", "r")
array = f.readline().split()
for i in range(len(array)):
    array[i] = int(array[i])
print(array)
f.close()
help = []

timp = 0
for i in range(len(array)):
    timp += int(array[i])
    help.append(timp)
x = format(sum(help)/len(help), '.2f')
print("timpul mediu de așteptare inițial va fi: ", x)

help.clear()
timp = 0
array.sort()
for i in range(len(array)):
    timp += int(array[i])
    help.append(timp)
x = format(sum(help)/len(help), '.2f')
print("timpul mediu de așteptare după sortarea listei va fi: ", x)



