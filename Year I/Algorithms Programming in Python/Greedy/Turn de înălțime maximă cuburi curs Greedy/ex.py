# 3. Turn de înălțime maximă format din cuburi
# Se dă o mulțime de n cuburi. Fiecare cub este caracterizat prin lungimea laturii și culoare. Nu există
# două cuburi având aceeași dimensiune. Fișierul “cuburi.txt” conține pe prima linie un număr natural
# nenul n (numărul de cuburi), apoi pe următoarele n linii câte un număr natural nenul (lungimea laturii
# cubului) și un șir de caractere (culoarea cubului).
# Să se construiască un turn de înălțime maximă astfel încât peste un cub cu latura L și culoarea K se
# poate așeza doar un cub cu latura mai mică strict decât L și culoare diferită de K. În fișierul “turn.txt”
# să se afișeze componența turnului de la bază spre vârf, pe câte un rând latura și culoarea cubului, apoi
# la final să se afișeze înălțimea totală a turnului.
# Indicație de rezolvare:
# - Se sortează lista de cuburi descrescător după lungimea laturii.
# - La baza turnului se așază cubul de latură maximă, iar apoi se parcurge lista sortată și se adaugă
# la turn câte un cub care are culoare diferită de ultimul cub adăugat.

def latura(x):
    return int(x[0])

f = open("cuburi.txt", "r")
g = open("turn.txt", "w")

n = int(f.readline())

array = []
count = 0
for i in range(n):
    array.append(f.readline().split())
f.close()

array.sort(key=latura, reverse=True)
g.write(str(array[0][0]) + " " + str(array[0][1]) + '\n')
lastcube = array[0]
count += int(lastcube[0])
for i in range(1, n):
    if array[i][1] != lastcube[1]:
        g.write(str(array[i][0]) + " " + str(array[i][1]) + '\n')
        lastcube = array[i]
        count += int(lastcube[0])
g.write('\n' + "Inaltime totala: " + str(count))

