from random import choice, random, randint
import math

f = open("input.txt","r")
g = open("output.txt","w")

def input():
    population_dimension = int(f.readline().split()[0])

    l = f.readline()
    lim_inf = int(l.split()[0])
    lim_sup = int(l.split()[1])

    l = f.readline()
    a = int(l.split()[0])
    b = int(l.split()[1])
    c = int(l.split()[2])
    d = int(l.split()[3])

    precision = int(f.readline().split()[0])
    crossover = float(f.readline().split()[0])
    mutation = float(f.readline().split()[0])
    tries = int(f.readline().split()[0])
    return(population_dimension, lim_inf, lim_sup, a, b, c, d, precision, crossover, mutation, tries)


def cromosome_length(lim_inf, lim_sup, precision):
    # (lim_sup - lim_inf)*math.pow(10,precision) numarul de numere dintre lim sup si lim inf
    # log in baza 2 e de cati biti am nevoie sa codez atatea numere
    return math.ceil(math.log(((lim_sup - lim_inf)*math.pow(10,precision)),2)) 


def create_cromosome(l):
    x = []
    for _ in range(l):
        x.append(choice([0,1]))
    return x


def chromosome_to_float(chromosome, lim_inf ,lim_sup, l, precision):
    binary = ""
    for i in chromosome:
        binary += str(i)
    intul = int(binary,2)
    #formula curs pag 28
    floatul = ((lim_sup - lim_inf) / (pow(2,l) - 1)) *intul + lim_inf
    return round(floatul,precision)


def function(a,b,c,d,x):
    return(a*math.pow(x,3)+b*math.pow(x,2)+c*x+d)


def generate_probabilities(population_dimension, total_through_function, through_function):
    x = []
    global OUTPUTPTZ, OUTPUTPT
    for i in range(population_dimension):
        x.append(through_function[i] / total_through_function)

        #pt out
        if not OUTPUTPT:
            OUTPUTPTZ.append(through_function[i] / total_through_function)
    return x


def generare_v_incrucisare(population_dimension,IPS):
    global OUTPUTPT, pt_output2, pt_output3
    x = []
    # print(len(x))
    for _ in range(population_dimension):
        rand = random()

        if not OUTPUTPT:
            pt_output2.append(rand)

        y = binary_search(rand, IPS)
        x.append(y)

    if not OUTPUTPT:
        pt_output3 = x.copy()
    
    return x


def alegere_incrucisare(pt_incrucisare, population_dimension,crossover):
    global OUTPUTPT, pt_output4
    x = []
    for i in pt_incrucisare:
        a = random()
        if not OUTPUTPT:
            pt_output4.append(a)
        if a <= crossover:
            x.append(i)
    return x


def incrucisare(population, a, b, l):
    x = randint(0, l)
    y = randint(0, l) 
    c1 = population[a-1]
    c2 = population[b-1]
    #afisat x + doar partea din mijloc schimbata
    ras1 = []
    ras2 = []
    # for i in range(x):
    #     ras1.append(c1[i])
    #     ras2.append(c2[i])
    # for i in range(x,l):
    #     ras1.append(c2[i])
    #     ras2.append(c1[i])
    if(y<x):
        x,y=y,x
    for i in range(x):
        ras1.append(c1[i])
        ras2.append(c2[i])
    for i in range(x,y):
        ras1.append(c2[i])
        ras2.append(c1[i])
    for i in range(y,l):
        ras1.append(c1[i])
        ras2.append(c2[i])


    if not OUTPUTPT:
        pt_output5.append((x,a,b,ras1,ras2))
    return(ras1,ras2)

def incrucisare3(population, a, b, c, l):
    x = randint(0, l)
    c1 = population[a-1]
    c2 = population[b-1]
    c3 = population[c-1]
    #afisat x + doar partea din mijloc schimbata
    ras1 = []
    ras2 = []
    ras3 = []
    for i in range(x):
        ras1.append(c1[i])
        ras2.append(c2[i])
        ras3.append(c3[i])
    for i in range(x,l):
        ras1.append(c2[i])
        ras2.append(c3[i])
        ras3.append(c1[i])

    if not OUTPUTPT:
        pt_output5.append((x,a,b,ras1,ras2))
    return(ras1,ras2,ras3)



def mutation_func(population, mutation):
    global OUTPUTPT, pt_output7, pt_output8
    for c in population:
        for i in range(len(c)):
            prob = random()
            if prob < mutation:
                if not OUTPUTPT:
                    pt_output7.append(c)
                if c[i] == 0: 
                    c[i] = 1
                else: 
                    c[i] = 0 

    if not OUTPUTPT:
        pt_output8 = population.copy()
    return population


def binary_search(rand, IPS):
    left = 0
    right = len(IPS)
    while left <= right:
        mid = left + (right - left) // 2
        if IPS[mid] < rand:
            left = mid + 1
        else:
            right = mid - 1
    return left

population_dimension, lim_inf, lim_sup, a, b, c, d, precision, crossover, mutation, tries = input()
f.close()

l = cromosome_length(lim_inf, lim_sup, precision)
OUTPUTPT = False
OUTPUTPTX = []
OUTPUTPTY = []
OUTPUTPTZ = []
pt_output1 = []
pt_output2 = []
pt_output3 = []
pt_output4 = []
pt_output5 = []
pt_output6 = []
pt_output7 = []
pt_output8 = []
ptoutput10 = []
ptoutput11 = []

population = []
for _ in range(population_dimension):
    population.append(create_cromosome(l))

populatia_initiala = population.copy()

for _ in range(tries):
    floaturile = []
    for i in range(population_dimension):
        floaturile.append(chromosome_to_float(population[i], lim_inf, lim_sup, l, precision))

    # for i in floaturile:
    #     print(i)

    through_function = []
    for i in range(population_dimension):
        through_function.append(function(a,b,c,d,floaturile[i]))


    if not OUTPUTPT :
        OUTPUTPTX = floaturile.copy()
        OUTPUTPTY = through_function.copy()

    aux_nou = through_function.copy()
    aux_nou.sort(reverse=True)
    # print(aux_nou[0])
    # print()
    # print(aux_nou[0:2])

    elite1 = -1
    elite2 = -1

    justincase = [-1,-1]
    ajtr1 = []
    ajtr2 = []

    for i in range(population_dimension):
        ooo = function(a,b,c,d, chromosome_to_float(population[i], lim_inf, lim_sup, l, precision))
        if ooo == aux_nou[1] and ooo >= justincase[1] or ooo == aux_nou[0] and ooo >= justincase[0]:
            if elite1 == -1:
                elite1 = i
                justincase[0] = ooo
                ajtr1 = population[i]
            else:
                elite2 = i
                justincase[1] = ooo
                ajtr2 = population[i]

    nextgen = [population[elite1][:],population[elite2][:]]

    if nextgen[0] != ajtr1:
        nextgen[0] = ajtr1
    if nextgen[1] != ajtr2:
        nextgen[1] = ajtr2

    total_through_function = 0
    for i in through_function:
        total_through_function += i
        #print(i)

    # print(total_through_function)

    probabilities = generate_probabilities(population_dimension, total_through_function, through_function)

    s=0
    #intervale probabilitati selectie
    IPS = []
    for i in probabilities:
        IPS.append(s)
        s += i
    IPS.append(s)

    if not OUTPUTPT:
        pt_output1 = IPS

    #print(s)
    # print(IPS)

    pt_incrucisare = generare_v_incrucisare(population_dimension, IPS)

    newpopulation = population.copy()
    population = [newpopulation[i-1] for i in pt_incrucisare]

    alegere = alegere_incrucisare(pt_incrucisare, population_dimension, crossover)
    alegere_aux = []
    # if(len(alegere)==1):
    #     alegere_aux.append(alegere.pop)
    # #print(alegere)

    nealesi = []
    for i in range(population_dimension):
        if i not in alegere:
            nealesi.append(i)

    # if(len(alegere) %2 != 0):
    #     nealesi.append(alegere.pop())

    new = []
    # if(len(alegere)%2 != 0):
    while alegere != []:
        # print(len(alegere),end=" ")
        if len(alegere)==1:
            new.append(population[alegere[0]])
            alegere_aux.append(alegere.pop())
        elif len(alegere)!=3:
            # print("nu3")
            x1 = randint(0,len(alegere)-1)
            # print(x1)
            alegere_aux.append(alegere[x1])
            bb = alegere[x1]
            alegere.remove(bb)
            
            x2 = randint(0,len(alegere)-1)
            # print(x2)
            alegere_aux.append(alegere[x2])
            bb2 = alegere[x2]
            alegere.remove(bb2)
            x3, x4 = incrucisare(population, bb, bb2, l) 
            new.append(x3)
            new.append(x4)
        elif len(alegere)==3:
            # print("3")
            x1 = randint(0,len(alegere)-1)
            # print(x1)
            alegere_aux.append(alegere[x1])
            bb = alegere[x1]
            alegere.remove(bb)

            x2 = randint(0,len(alegere)-1)
            # print(x2)
            alegere_aux.append(alegere[x2])
            bb2 = alegere[x2]
            alegere.remove(bb2)

            x3 = randint(0,len(alegere)-1)
            # print(x2)
            alegere_aux.append(alegere[x3])
            bb3 = alegere[x3]
            alegere.remove(bb3)

            x4, x5, x6 = incrucisare3(population, bb, bb2, bb3, l) 
            new.append(x4)
            new.append(x5)
            new.append(x6)
    # else:
    #     while alegere != []:
    #         x1 = randint(0,len(alegere)-1)
    #         # print(x1)
    #         alegere_aux.append(alegere[x1])
    #         bb = alegere[x1]
    #         alegere.remove(alegere[x1])
    #         x2 = randint(0,len(alegere)-1)
    #         # print(x2)
    #         alegere_aux.append(alegere[x2])
    #         bb2 = alegere[x2]
    #         alegere.remove(alegere[x2])
    #         x3, x4 = incrucisare(population, bb, bb2, l) 
    #         new.append(x3)
    #         new.append(x4)

    # print(alegere_aux)
    for i in new:
        population.append(i)

    if not OUTPUTPT:
        pt_output6 = population.copy()

    for i in alegere_aux:
        population.remove(population[i])
        for y in range(len(alegere_aux)):
            alegere_aux[y]-=1

    population = mutation_func(population, mutation)


    # floaturile2 = []
    # for i in range(population_dimension):
    #     floaturile2.append(chromosome_to_float(population[i], lim_inf, lim_sup, l, precision))

    # through_function2 = []
    # for i in range(population_dimension):
    #     through_function2.append(function(a,b,c,floaturile[i]))

    aux_nou.sort()

    e1 = -1
    e2 = -1

    for i in range(population_dimension):
        if function(a,b,c,d, chromosome_to_float(population[i], lim_inf, lim_sup, l, precision)) == aux_nou[1] or function(a,b,c,d, chromosome_to_float(population[i], lim_inf, lim_sup, l, precision)) == aux_nou[0] :
            if e1 == -1:
                e1 = i
            else:
                e2 = i

    population.remove(population[e1])
    e2-=1
    population.remove(population[e2])


    population.extend(nextgen)
    ptoutput10.append(max(through_function))

    for i in range(len(through_function)):
        if(through_function[i] == max(through_function)):
            val_noua_index_maxim = i
            
    ptoutput11.append(floaturile[i])


    OUTPUTPT = True

    # lista = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    # ll = chromosome_to_float(lista, lim_inf, lim_sup, l, precision)
    # print(ll)

g.write("Populatia initiala\n")
for i in range(population_dimension):
    if i <= 8:
        g.write(str(i+1)+":  "+str(populatia_initiala[i])+ "  x = "+ str(OUTPUTPTX[i]) + "    f = " + str(OUTPUTPTY[i]) + '\n')
    else:
        g.write(str(i+1)+": "+str(populatia_initiala[i])+ "  x = "+ str(OUTPUTPTX[i]) + "     f = " + str(OUTPUTPTY[i])  + '\n')
g.write('\n')
g.write("Probabilitati selectie\n")
for i in range(population_dimension):
    if i <= 8:
        g.write(str(i+1)+":  "+str(OUTPUTPTZ[i]) + '\n')
    else:
        g.write(str(i+1)+": "+str(OUTPUTPTZ[i]) + '\n')
g.write('\n')
g.write("Intervale robabilitati selectie\n")
g.write("0 ")
for i in range(1,len(pt_output1)):
    g.write(str(pt_output1[i]) + " ")
    if i % 5 == 0:
        g.write('\n')
g.write('\n')
for i in range(population_dimension):
    g.write("u = "+str(pt_output2[i]) + "  =>  cromozomul "+str(pt_output3[i])+'\n')
g.write('\n')

g.write("Dupa selectie\n")
for i in range(population_dimension):
    if i <= 8:
        g.write(str(i+1)+":  "+str(populatia_initiala[pt_output3[i]-1])+ "  x = "+ str(OUTPUTPTX[pt_output3[i]-1]) + "    f = " + str(OUTPUTPTY[pt_output3[i]-1]) + '\n')
    else:
        g.write(str(i+1)+": "+str(populatia_initiala[pt_output3[i]-1])+ "  x = "+ str(OUTPUTPTX[pt_output3[i]-1]) + "     f = " + str(OUTPUTPTY[pt_output3[i]-1])  + '\n')
g.write('\n')

g.write("Probabilitatea de incrucisare "+str(crossover)+ "\n")
for i in range(population_dimension):
    if i <= 8:
        if(pt_output4[i] <= crossover):
            g.write(str(i+1)+":  "+str(pt_output4[i]) + "  participa \n")
        else:
            g.write(str(i+1)+":  "+str(pt_output4[i]) + '\n')
    else:
        if(pt_output4[i] <= crossover):
            g.write(str(i+1)+":  "+str(pt_output4[i]) + "  participa \n")
        else:
            g.write(str(i+1)+": "+str(pt_output4[i]) + '\n')
g.write('\n')

for j in range (0,len(pt_output5),1):
    g.write("\nRecombinare dintre cromozomii "+ str(pt_output5[j][0]+1) + " si " + str(pt_output5[j][1]+1) + " la taietura " + str(pt_output5[j][2]) + "\nSi rezulta " + str(pt_output5[j][3]) + " si " + str(pt_output5[j][4]))

g.write("\n\nDupa recombinare\n")
for i in range(population_dimension):
    if i <= 8:
        g.write(str(i+1)+":  "+str(pt_output6[i])+ "  x = "+ str(chromosome_to_float(pt_output6[i],lim_inf, lim_sup, l, precision)) + "    f = " + str(function(a, b, c,d, chromosome_to_float(pt_output6[i],lim_inf, lim_sup, l, precision))) + '\n')
    else:
        g.write(str(i+1)+": "+str(pt_output6[i])+ "  x = "+ str(chromosome_to_float(pt_output6[i],lim_inf, lim_sup, l, precision)) + "     f = " + str(function(a, b, c,d, chromosome_to_float(pt_output6[i],lim_inf, lim_sup, l, precision))) + '\n')
g.write('\n')

g.write("Probabilitati de mutatie "+str(mutation))
g.write("\nAu fost modificate genele:")
for i in range(len(pt_output7)):
    g.write(" "+ str(pt_output8.index(pt_output7[i])+1))
g.write('\n')
for i in range(population_dimension):
    if i <= 8:
        g.write(str(i+1)+":  "+str(pt_output8[i])+ "  x = "+ str(chromosome_to_float(pt_output8[i],lim_inf, lim_sup, l, precision)) + "    f = " + str(function(a, b, c,d, chromosome_to_float(pt_output8[i],lim_inf, lim_sup, l, precision))) + '\n')
    else:
        g.write(str(i+1)+": "+str(pt_output8[i])+ "  x = "+ str(chromosome_to_float(pt_output8[i],lim_inf, lim_sup, l, precision)) + "     f = " + str(function(a, b, c,d, chromosome_to_float(pt_output8[i],lim_inf, lim_sup, l, precision))) + '\n')
g.write('\n')

g.write("Evolutia maximului")
for i in range(len(ptoutput10)):
    g.write('\n'+str(ptoutput10[i]) + " x = " +str(ptoutput11[i]))
g.write("\nValoarea medie a performantei\n" + str(sum(ptoutput10)/len(ptoutput10)))


g.close()