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