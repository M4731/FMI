"""
7. Știind că 1 ianuarie 1702 a picat într-o zi de duminică, să se citească de la tastatură o dată mai
recentă, și să se spună în ce zi a săptămânii cade aceasta.
Puteți să faceți 2 cazuri - în care inputul este dat de forma "1 10 2019", sau "1 octombrie 2019".
Folosiți funcția range() pentru a itera printre ani, respectiv instrucțiuni if/elif/else pentru a trata
cazurile de ani bisecți. Puteți folosi un dicționar sau o listă pe post de switch/case ca să aflați în ce zi a
săptămânii pică data respectivă.
Formula pentru an bisect (leap year) este:
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
"""
def isLeap(year):
    leap = False
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            leap = True
    return leap

zile = {
    0: 'Luni',
    1: 'Marti',
    2: 'Miercuri',
    3: 'Joi',
    4: 'Vineri',
    5: 'Sambata',
    6: 'Duminica'
}
zi = int(input("ziua: "))
luna = int(input("luna: "))
an = int(input("anul: "))

baseYear = 1970
baseMonth = 1
nrZile = 0

while baseYear < an:
    if isLeap(baseYear):
        nrZile += 1
    nrZile += 365
    baseYear += 1
while baseMonth < luna:
    if baseMonth == 2 and isLeap(an):
        nrZile += 29
    elif baseMonth == 2 and isLeap(an) == 0:
        nrZile += 28
    elif baseMonth % 2 == 1:
        nrZile += 31
    else:
        nrZile += 30
    baseMonth += 1
nrZile += zi - 1

print(zile[((nrZile % 7) + 3) % 7])