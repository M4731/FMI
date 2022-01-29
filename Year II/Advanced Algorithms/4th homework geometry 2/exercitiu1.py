def read():
    f=open("ex1_input.txt", "r")

    n=int(f.readline())
    semiplans = []
    for x in range(n):
        l=f.readline().split()
        a=float(l[0])
        b=float(l[1])
        c=float(l[2])
        semiplans.append((a,b,c))

    f.close()
    return n, semiplans


def normalize(h, v):
    new_h = []
    new_v = []
    for x in h:
        aux = []
        for i in x:
            aux.append(i / abs(x[0]))
        new_h.append(aux)
    for x in v:
        aux = []
        for i in x:
            aux.append(i / abs(x[1]))
        new_v.append(aux)
    return new_h, new_v


def intersection(h, v):
    lim_left = None
    lim_right = None
    lim_down = None
    lim_up = None
    lim = True

    aux = [i[2] for i in h if i[0] < 0]
    if aux != []:
        lim_left = min(aux)
    else:
        lim = False

    aux = [i[2] for i in h if i[0] > 0]
    if aux != []:
        lim_right = max(aux)
    else:
        lim = False

    aux = [i[2] for i in v if i[1] < 0]
    if aux != []:
        lim_down = min(aux)
    else:
        lim = False

    aux = [i[2] for i in v if i[1] > 0]
    if aux != []:
        lim_up = max(aux)
    else:
        lim = False

    if lim_down and lim_up:
        if lim_down < -lim_up:
            if not lim:
                return -1
                # nevida nemarginita

    if lim_left and lim_right:
        if lim_left < -lim_right:
            if not lim:
                return -1
                # nevida nemarginita
            else:
                return 0
                # nevida marginita

    return 1
    # vida

if __name__=="__main__":
    n, semiplans = read()

    h = []
    v = []
    for x in semiplans:
        if(x[0] == 0):
            v.append(x)
        elif(x[1] == 0):
            h.append(x)

    h,v = normalize(h, v)
    
    result = intersection(h,v)

    if result == -1:
        print("nevida nemarginita")
    elif result == 0:
        print("nevida marginita")
    else:
        print("vida")