def viraj(P, Q, R):
    return((Q[1] - P[1]) * (R[0] - Q[0]) - (Q[0] - P[0]) * (R[1] - Q[1]))

if __name__ == "__main__":
    f = open("coord.in","r")
    P = tuple(float(i) for i in f.readline().split())
    Q = tuple(float(i) for i in f.readline().split())
    R = tuple(float(i) for i in f.readline().split())

    if(viraj(P,Q,R) == 0): 
        print("Puncte coliniare.")
    elif(viraj(P,Q,R) < 0):
        print("Viraj la stanga.")
    else:
        print("Viraj la dreapta.")

    f.close()