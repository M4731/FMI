import copy
import time
import os
import stopit
import sys
from math import sqrt

increment = -1

class NodParcurgere:
	def __init__(self, id, info, parinte, cost, euristic, boots, bag):
		global increment
		increment+=1
		self.nr_ordine = increment
		self.id=id # este indicele din vectorul de noduri
		self.info=info
		self.parinte=parinte #parintele din arborele de parcurgere
		self.cost=cost #acesta este costul de la nodul de start (radacina arborelui de parcurgere) pana la nodul curent
		self.boots=boots
		self.bag=bag
		self.euristic=euristic
		self.rock=False
		self.f=self.cost+self.euristic


	def obtineDrum(self):
		l=[(self.info,self.id,self.nr_ordine)]
		nod=self
		while nod.parinte is not None:
			x = (nod.parinte.info, nod.parinte.id,nod.nr_ordine)
			l.insert(0, x)
			nod=nod.parinte
		return l
		
	def afisDrum(self, file): #returneaza si lungimea drumului
		g = open(file, "a")
		g.write("Solutie: ")
		l=self.obtineDrum()
		# print(l)
		g.write("("+str(l[0][2])+")"+str(l[0][0])+str(l[0][1]))
		# print("("+str(l[0][2])+")"+str(l[0][0])+str(l[0][1]),end=" ")
		for x in range(1,len(l)):
			# print("-> ("+str(l[x][2])+")"+str(l[x][0])+str(l[x][1]),end=" ")
			g.write("-> ("+str(l[x][2])+")"+str(l[x][0])+str(l[x][1]))
		# print("\nCost: ",self.cost)
		g.write("\nCost: "+str(self.cost)+'\n')
		# print("Lungime: ",len(l))
		g.write("Lungime: "+str(len(l))+'\n')
		g.write("----------------------\n")
		g.close()
		return len(l)


	def contineInDrum(self, infoNodNou):
		nodDrum=self
		while nodDrum is not None:
			if(infoNodNou==nodDrum.info):
				return True
			nodDrum=nodDrum.parinte
		
		return False
		
	def __repr__(self):
		sir=""		
		sir+=self.info+"("
		sir+="id = {}, ".format(self.id)
		sir+="drum="
		drum=self.obtineDrum()
		# sir+=("->").join(str(drum))
		# for x in drum:
		# 	sir+= str(x[2]) + str(x[0]) + str(x[1]) + "->"
		if self.parinte != None:
			sir+=" parinte:{}".format(self.parinte.id)
		sir+=" cost:{}".format(self.cost)
		sir+=" h:{}".format(self.euristic)
		sir+=" boots:{}".format(self.boots)
		sir+=" bag:{})".format(self.bag)
		return(sir)

class Graph: #graful problemei
	def __init__(self, colours_matrix, map_matrix, start, finish, costs, boots, bag, rock):
		# self.noduri=noduri
		self.colours_matrix=colours_matrix
		self.map_matrix=map_matrix
		self.start=start
		self.finish=finish
		self.costs=costs
		self.boots=boots
		self.bag=bag
		self.rock=rock

	# def indiceNod(self, n):
	# 	return self.noduri.index(n)

	def testeaza_scop(self, nodCurent):
		return nodCurent.rock==True
		# return nodCurent.id == self.finish

	def testeaza_exit(self, nodCurent):
		return self.rock==True and nodCurent.id==self.finish

	def update_bootsnstone(self, nodCurent):
		#metoda de updatare a ghetelor si a ghiozdanului in momentul in care micul vrajitor intra intr-o incapere noua
		nodCurent = copy.deepcopy(nodCurent)
		pc = self.map_matrix[nodCurent.id[0]][nodCurent.id[1]]
		# print(pc)
		if pc != '0' and pc != '*':
			if pc == '@':
				nodCurent.rock = True
			else:
				if nodCurent.bag[1] == None:
					nodCurent.bag[1] = 0
					nodCurent.bag[0] = pc
				elif nodCurent.boots[1] > 2:
					nodCurent.boots[0] = pc
					nodCurent.boots[1] = 0
				elif nodCurent.bag[1] > 2:
					nodCurent.bag[0] = pc
					nodCurent.bag[1] = 0
				else:
					nodCurent.bag[1] = 0
					nodCurent.bag[0] = pc
		return nodCurent

	def compute_eur2(self, point):
		#euristica
		#distanta manhattan fata de (start+finish)/2
		x1=abs(self.finish[0] - self.finish[1]) + abs(point[0] - point[1])
		x2=abs(self.start[0] - self.start[1]) + abs(point[0] - point[1])
		x = (x1+x2)//2

		return x

	def compute_eur3(self, point):
		#euristica
		#distanta euclidiana fata de (start+finish)/2
		x1=sqrt(pow(self.finish[0] - self.finish[1],2) + pow(point[0] - point[1],2))
		x2=sqrt(pow(self.start[0] - self.start[1],2) + pow(point[0] - point[1],2))
		x = (x1+x2)//2

		return x

	def compute_eur4(self, point):
		#euristica
		#inadmisibila
		x1=abs(self.finish[0] - self.finish[1]) + abs(point[0] - point[1])
		x2=abs(self.start[0] - self.start[1]) + abs(point[0] - point[1])
		x = point[0]+point[1]

		return x

	#va genera succesorii sub forma de noduri in arborele de parcurgere	
	def genereazaSuccesori(self, nodCurent, tip_euristica = 1):
		#metoda genereaza succesori care verifica daca vrajitorul poate merge in sus/jos/stanga/dreapta pe matrice 
		#avand in vedere ghetele cu care este incaltat si ghetele pe care le are in ghiozdan
		global increment
		euristic_value = 0
		listaSuccesori=[]
		if nodCurent.id[0]!=0:
			up = (nodCurent.id[0]-1, nodCurent.id[1])
			if tip_euristica == 2:
				euristic_value = self.compute_eur2(up)
			if tip_euristica == 3: 
				euristic_value = self.compute_eur3(up)
			if tip_euristica == 4: 
				# print('a')
				euristic_value = self.compute_eur4(up)
			colour =  self.colours_matrix[up[0]][up[1]]
			if nodCurent.parinte != None and nodCurent.parinte.id != up or nodCurent.parinte == None:
				if nodCurent.boots[0] == colour and nodCurent.boots[1] < 3:# or nodCurent.bag[0] == colour and nodCurent.bag[1] < 3:
					pc = NodParcurgere(up, colour, nodCurent, nodCurent.cost + self.costs[colour], euristic_value, [nodCurent.boots[0],nodCurent.boots[1]+1], nodCurent.bag)
					pc = self.update_bootsnstone(pc)
					listaSuccesori.append(pc)
				elif nodCurent.bag[0] == colour and nodCurent.bag[1] < 3:
					pc = NodParcurgere(up, colour, nodCurent, nodCurent.cost + self.costs[colour], euristic_value, [nodCurent.bag[0],nodCurent.bag[1]+1], nodCurent.boots)
					pc = self.update_bootsnstone(pc)
					listaSuccesori.append(pc)

		if nodCurent.id[0]!=len(self.colours_matrix)-1:
			down = (nodCurent.id[0]+1, nodCurent.id[1])
			if tip_euristica == 2:
				euristic_value = self.compute_eur2(down)
			if tip_euristica == 3: 
				euristic_value = self.compute_eur3(down)
			if tip_euristica == 4: 
				euristic_value = self.compute_eur4(down)
			# colour =  self.colours_matrix[up[0]][up[1]]
			colour =  self.colours_matrix[down[0]][down[1]]
			if nodCurent.parinte != None and nodCurent.parinte.id != down or nodCurent.parinte == None:
				if nodCurent.boots[0] == colour and nodCurent.boots[1] < 3:
					pc = NodParcurgere(down, colour, nodCurent, nodCurent.cost + self.costs[colour], euristic_value, [nodCurent.boots[0],nodCurent.boots[1]+1], nodCurent.bag)
					pc = self.update_bootsnstone(pc)
					listaSuccesori.append(pc)
				elif nodCurent.bag[0] == colour and nodCurent.bag[1] < 3:
					pc = NodParcurgere(down, colour, nodCurent, nodCurent.cost + self.costs[colour], euristic_value, [nodCurent.bag[0],nodCurent.bag[1]+1], nodCurent.boots)
					pc = self.update_bootsnstone(pc)
					listaSuccesori.append(pc)
		
		if nodCurent.id[1]!=0:
			# print('m')
			# print(nodCurent)
			left = (nodCurent.id[0], nodCurent.id[1]-1)
			if tip_euristica == 2:
				euristic_value = self.compute_eur2(left)
			if tip_euristica == 3: 
				euristic_value = self.compute_eur3(left)
			if tip_euristica == 4: 
				euristic_value = self.compute_eur4(left)
			# colour =  self.colours_matrix[up[0]][up[1]]
			colour =  self.colours_matrix[left[0]][left[1]]
			# print(left)
			# print(nodCurent.boots[0])
			# print(colour)
			if nodCurent.parinte != None and nodCurent.parinte.id != left or nodCurent.parinte == None:
				if nodCurent.boots[0] == colour and nodCurent.boots[1] < 3:
					pc = NodParcurgere(left, colour, nodCurent, nodCurent.cost + self.costs[colour], euristic_value, [nodCurent.boots[0],nodCurent.boots[1]+1], nodCurent.bag)
					pc = self.update_bootsnstone(pc)
					listaSuccesori.append(pc)
				elif nodCurent.bag[0] == colour and nodCurent.bag[1] < 3:
					pc = NodParcurgere(left, colour, nodCurent, nodCurent.cost + self.costs[colour], euristic_value, [nodCurent.bag[0],nodCurent.bag[1]+1], nodCurent.boots)
					# print("nod curent",nodCurent.boots)
					# print(pc.boots)
					# print(pc.bag)
					pc = self.update_bootsnstone(pc)
					# print("nod curent",nodCurent.boots)
					# print(pc.boots)
					# print(pc.bag)
					listaSuccesori.append(pc)
		
		if nodCurent.id[1]!=len(self.map_matrix[0])-1:
			right = (nodCurent.id[0], nodCurent.id[1]+1)
			if tip_euristica == 2:
				euristic_value = self.compute_eur2(right)
			if tip_euristica == 3: 
				euristic_value = self.compute_eur3(right)
			if tip_euristica == 4: 
				euristic_value = self.compute_eur4(right)
			# colour =  self.colours_matrix[up[0]][up[1]]
			colour =  self.colours_matrix[right[0]][right[1]]
			# print(nodCurent.boots[0],colour)
			if nodCurent.parinte != None and nodCurent.parinte.id != right or nodCurent.parinte == None:
				if nodCurent.boots[0] == colour and nodCurent.boots[1] < 3:
					# print('m')
					pc = NodParcurgere(right, colour, nodCurent, nodCurent.cost + self.costs[colour], euristic_value, [nodCurent.boots[0],nodCurent.boots[1]+1], nodCurent.bag)
					pc = self.update_bootsnstone(pc)
					listaSuccesori.append(pc)
				elif nodCurent.bag[0] == colour and nodCurent.bag[1] < 3:
					pc = NodParcurgere(right, colour, nodCurent, nodCurent.cost + self.costs[colour], euristic_value, [nodCurent.bag[0],nodCurent.bag[1]+1], nodCurent.boots)
					pc = self.update_bootsnstone(pc)
					listaSuccesori.append(pc)

		return listaSuccesori


	def __repr__(self):
		sir=""
		for (k,v) in self.__dict__.items() :
			sir+="{} = {}\n".format(k,v)
		return(sir)

def read(folder, inputt):
	#functie care ne ajuta cu citirea inputului
    listaFisiere=os.listdir(folder)
    f = open(f"./{folder}/{listaFisiere[inputt-1]}","r")

    l = f.read()
    l = l.split("----")
    l[0] = l[0].split()
    costs = {}
    for i in range(0,len(l[0])-1,2):
        costs[l[0][i]] = int(l[0][i+1])

    l[1] = l[1].split('\n')
    l[1].remove(l[1][0])

    colours_matrix = []
    for i in range(len(l[1])//2):
        line = l[1][i].split()
        colours_matrix.append(line)

    map_matrix = []
    for i in range(len(l[1])//2+1,len(l[1])):
        line = l[1][i].split()
        map_matrix.append(line)

    f.close()
    return costs, colours_matrix, map_matrix

def refresh_files():
	#functie care da refresh la output de fiecare data cand rulam programul deoarece toate cele lalte functii dau append si outputul nu s-ar sterge niciodata

	if not os.path.exists("output"):
		os.mkdir("output")

	f= open("./output/ucs_output.txt","w")
	f.write("UCS\n\n")
	f.close()

	f= open("./output/astar_output.txt","w")
	f.write("A STAR\n\n")
	f.close()

	f= open("./output/astaropt_output.txt","w")
	f.write("A STAR OPTIMIZAT\n\n")
	f.close()

	f= open("./output/idastar_output.txt","w")
	f.write("IDA STAR\n\n")
	f.close()	

#rularea dinamica de 2 ori a alogoritmulor face posibila intoarcerea vrajitorului la iesirea din pestera dupa ce a luat piatra
@stopit.threading_timeoutable(default="UCS TIMEOUT")
def uniform_cost(gr, shoes, bag, nrSolutiiCautate=1):
	
	start_time = time.time()
	maxim_coada = 0
	maxim_generat = 0
	global increment 
	increment = 0

	c=[NodParcurgere(gr.start, gr.colours_matrix[gr.start[0]][gr.start[1]], None, 0, 0, shoes, bag)]
	
	while len(c)>0:
		# print("Coada actuala: " + str(c))
		# input()

		maxim_coada = max(maxim_coada,len(c))
		nodCurent=c.pop(0)

		# print("boots ",nodCurent.boots)
		# print("bag ",nodCurent.bag)
		# print(nodCurent.id, gr.finish)
		if gr.testeaza_scop(nodCurent):
			g.finish = start
			g.start = finish
			g.rock = True

			uniform_cost(g,shoes,bag,nrSolutiiCautate)

		if gr.testeaza_exit(nodCurent):
			# print("Solutie: ", end="")
			nodCurent.afisDrum("./output/ucs_output.txt")
			# print("\n----------------\n")
			nrSolutiiCautate-=1
			if nrSolutiiCautate==0:
				# print('m')
				end_time = time.time()
				gout = open("./output/ucs_output.txt","a")
				# print("Timp executie: "+ str(end_time-start_time))
				gout.write("Timp executie: "+ str(end_time-start_time)+'\n')
				# print("Nr maxim de noduri existente la un moment dat in memorie: " + str(maxim_coada))
				gout.write("Nr maxim de noduri existente la un moment dat in memorie: " + str(maxim_coada)+'\n')
				# print("Nr total de noduri generate: " + str(maxim_generat))
				gout.write("Nr total de noduri generate: " + str(maxim_generat)+'\n')

				g.finish = finish
				g.start = start
				g.rock = False
				return "UCS FINISHED"

		lSuccesori=gr.genereazaSuccesori(nodCurent)	
		maxim_generat += len(lSuccesori)
		# print(lSuccesori)
		for s in lSuccesori:
			i=0
			gasit_loc=False
			for i in range(len(c)):
				#ordonez dupa cost(notat cu g aici și în desenele de pe site)
				if c[i].cost>s.cost :
					gasit_loc=True
					break
			if gasit_loc:

				c.insert(i,s)
			else:
				c.append(s)

@stopit.threading_timeoutable(default="ASTAR TIMEOUT")
def a_star(gr, shoes, bag, nrSolutiiCautate=1, tip_euristica=1):
	start_time = time.time()
	maxim_coada = 0
	maxim_generat = 0
	global increment 
	increment = 0

	c=[NodParcurgere(gr.start, gr.colours_matrix[gr.start[0]][gr.start[1]], None, 0, 0, shoes, bag)]
	
	while len(c)>0:
		maxim_coada = max(maxim_coada,len(c))
		nodCurent=c.pop(0)
		# print(nodCurent)
		
		if gr.testeaza_scop(nodCurent):
			g.finish = start
			g.start = finish
			g.rock = True

			a_star(g,shoes,bag,nrSolutiiCautate,tip_euristica)

		if gr.testeaza_exit(nodCurent):
			nodCurent.afisDrum("./output/astar_output.txt")
			nrSolutiiCautate-=1
			if nrSolutiiCautate==0:
				end_time = time.time()
				gout = open("./output/astar_output.txt","a")
				gout.write("Timp executie: "+ str(end_time-start_time)+'\n')
				gout.write("Nr maxim de noduri existente la un moment dat in memorie: " + str(maxim_coada)+'\n')
				gout.write("Nr total de noduri generate: " + str(maxim_generat)+'\n')

				g.finish = finish
				g.start = start
				g.rock = False
				return "ASTAR FINISHED"

		lSuccesori=gr.genereazaSuccesori(nodCurent,tip_euristica)	
		maxim_generat += len(lSuccesori)
		for s in lSuccesori:
			i=0
			gasit_loc=False
			for i in range(len(c)):
				#diferenta fata de UCS e ca ordonez dupa f
				if c[i].f>=s.f :
					gasit_loc=True
					break
			if gasit_loc:
				c.insert(i,s)
			else:
				c.append(s)

@stopit.threading_timeoutable(default="ASTAR OPTIMIZED TIMEOUT")
def a_star_optimized(gr, shoes, bag, tip_euristica=1):
	
	# print(g.start, g.finish)
	l_open=[NodParcurgere(gr.start, gr.colours_matrix[gr.start[0]][gr.start[1]], None, 0, 0, shoes, bag)]
	
	start_time = time.time()
	maxim_coada = 0
	maxim_generat = 0
	global increment 
	increment = 0

	#l_closed contine nodurile expandate
	l_closed=[]

	while len(l_open)>0:

		# print("Coada actuala: " + str(l_open))
		# print("Coada closed: " + str(l_closed))
		# input()
		# print(g.rock)
		maxim_coada = max(maxim_coada,len(l_open)+len(l_closed))
		nodCurent=l_open.pop(0)
		# print(nodCurent)
		l_closed.append(nodCurent)

		if gr.testeaza_scop(nodCurent):
			g.finish = start
			g.start = finish
			g.rock = True
			# print('m')
			l_closed = []
			l_open = []
			a_star_optimized(g,shoes,bag, tip_euristica)


		if gr.testeaza_exit(nodCurent):
			# print('c')
			nodCurent.afisDrum("./output/astaropt_output.txt")
			end_time = time.time()
			gout = open("./output/astaropt_output.txt","a")
			gout.write("Timp executie: "+ str(end_time-start_time)+'\n')
			gout.write("Nr maxim de noduri existente la un moment dat in memorie: " + str(maxim_coada)+'\n')
			gout.write("Nr total de noduri generate: " + str(maxim_generat)+'\n')
			# print('m')
			g.finish = finish
			g.start = start
			g.rock = False
			return "ASTAR OPTIMIZED FINISHED"

		lSuccesori=gr.genereazaSuccesori(nodCurent)	
		maxim_generat += len(lSuccesori)
		# print(lSuccesori)
		for s in lSuccesori:
			gasitC=False
			for nodC in l_open:
				if s.id==nodC.id:
					gasitC=True
					if s.f>=nodC.f:
						lSuccesori.remove(s)
					else:#s.f<nodC.f
						l_open.remove(nodC)
					break
			if not gasitC:
				for nodC in l_closed:
					if s.id==nodC.id:
						if s.f>=nodC.f:
							lSuccesori.remove(s)
						else:#s.f<nodC.f
							l_closed.remove(nodC)
						break
		for s in lSuccesori:
			i=0
			gasit_loc=False
			for i in range(len(l_open)):
				#diferenta fata de UCS e ca ordonez crescator dupa f
				#daca f-urile sunt egale ordonez descrescator dupa g
				if l_open[i].f>s.f or (l_open[i].f==s.f and l_open[i].cost<=s.cost) :
					gasit_loc=True
					break
			if gasit_loc:
				l_open.insert(i,s)
			else:
				l_open.append(s)

#am incercat..
@stopit.threading_timeoutable(default="IDASTAR TIMEOUT")
def ida_star(gr, shoes, bag, nrSolutiiCautate=1, tip_euristica=1):
	
	start_time = time.time()
	maxim_coada = 0
	maxim_generat = 0
	global increment 
	increment = 0
	nodStart=NodParcurgere(gr.start, gr.colours_matrix[gr.start[0]][gr.start[1]], None, 0, 0, shoes, bag)
	limita=nodStart.f
	while True:

		nrSolutiiCautate, rez= construieste_drum(gr, nodStart,limita,nrSolutiiCautate,start_time, maxim_coada, maxim_generat, shoes, bag, tip_euristica)
		if rez=="gata":
			break
		if rez==float('inf'):
			print("Nu exista solutii!")
			break
		limita=rez
	
	return "IDASTAR FINISHED"

#...
def construieste_drum(gr, nodCurent, limita, nrSolutiiCautate, start_time, maxim_coada, maxim_generat, shoes, bag, tip_euristica):
	if nodCurent.f>limita:
		return nrSolutiiCautate, nodCurent.f

	if gr.testeaza_scop(nodCurent):
		g.finish = start
		g.start = finish
		g.rock = True

		ida_star(g,shoes,bag,nrSolutiiCautate, tip_euristica)

	if gr.testeaza_exit(nodCurent):
		nodCurent.afisDrum("./output/idastar_output.txt")
		nrSolutiiCautate-=1
		if nrSolutiiCautate==0:
			end_time = time.time()
			gout = open("./output/idastar_output.txt","a")
			gout.write("Timp executie: "+ str(end_time-start_time)+'\n')
			gout.write("Nr maxim de noduri existente la un moment dat in memorie: " + str(maxim_coada)+'\n')
			gout.write("Nr total de noduri generate: " + str(maxim_generat)+'\n')

			g.finish = finish
			g.start = start
			g.rock = False
			return 0,"gata"

	lSuccesori=gr.genereazaSuccesori(nodCurent,tip_euristica)	
	minim=float('inf')
	for s in lSuccesori:
		nrSolutiiCautate, rez=construieste_drum(gr, s, limita, nrSolutiiCautate,start_time, maxim_coada, maxim_generat, shoes, bag, tip_euristica)
		if rez=="gata":
			return 0,"gata"
		if rez<minim:
			minim=rez
	return nrSolutiiCautate, minim

if __name__ == "__main__":
    
	#exemplu rulare python little_wizard.py 1 2 3 input 3
    refresh_files()

    t = int(sys.argv[1])
    euristica = int(sys.argv[2])
    nsol = int(sys.argv[3])
    folder = sys.argv[4]
    inputt = int(sys.argv[5])

    costs, colours_matrix, map_matrix = read(folder, inputt)
    start = ()
    finish = ()
    bag = [None, None]
    shoes = [None, None]
    rock = False

    for line in range(len(map_matrix)):
        for col in range(len(map_matrix[line])):
            if map_matrix[line][col] == '*':
                start = (line,col)
                shoes.append(colours_matrix[line][col])
                shoes.append(1)
            if map_matrix[line][col] == '@': finish = (line,col)

	# shoes = [colours_matrix[start[0]][start[1]],0]
    shoes = [colours_matrix[start[0]][start[1]], 1]

    g = Graph(colours_matrix, map_matrix, start, finish, costs, shoes, bag, False)
    # print(g.genereazaSuccesori(NodParcurgere((3,3), 'r', None, 0, ['r',0], ['a',0])))
    uniform_cost(g,shoes,bag,nsol, timeout=t)
    a_star(g, shoes, bag, nsol, euristica, timeout=t)
    a_star_optimized(g, shoes, bag,euristica, timeout=t)
    ida_star(g, shoes, bag,nsol,euristica, timeout=t)