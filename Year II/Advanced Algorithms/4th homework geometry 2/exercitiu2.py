import math
from os import X_OK

def read():
    f=open("ex2_input.txt", "r")

    inputq = f.readline().split()
    q1 = float(inputq[0])
    q2 = float(inputq[1])

    n=int(f.readline())
    semiplans = []
    for x in range(n):
        l=f.readline().split()
        a=float(l[0])
        b=float(l[1])
        c=float(l[2])
        semiplans.append((a,b,c))

    return (q1,q2), n, semiplans


def calc(x, c):
    if x < 0:
        return - (-c / abs(x))
    else:
        return -(c / abs(x))


def dreptunghi(Q, h, v):
    left = -math.inf
    right = math.inf
    down = -math.inf
    up = math.inf
    sem = False

    for x in v:
        if x < Q[0] and Q[0] - x <= Q[0] - left:
            left = x
        if x > Q[0] and x - Q[0] <= right - Q[0]:
            right = x
        if x == Q[0]:
            sem = True
    if sem:
        stanga = Q[0] - left
        dreapta = right - Q[0]
        if stanga > dreapta:
            left = Q[0]
        else:
            right = Q[0]

    sem = False

    for x in h:
        if x < Q[1] and Q[1] - x <= Q[1] - down:
            down = x
        if x > Q[1] and x - Q[1] <= up - Q[1]:
            up = x
        if x == Q[1]:
            sem = True
    if sem:
        sus = up - Q[1]
        jos = Q[1] - down
        if sus > jos:
            up = Q[1]
        else:
            down = Q[1]

    return left, right, down, up


if __name__=="__main__":
    Q, n, semiplans = read()

    v = []
    h = []

    for x in semiplans:
        if x[0] != 0:
            v.append(calc(x[0], x[2]))
        if x[1] != 0:
            h.append(calc(x[1], x[2]))

    left, right, down, up = dreptunghi(Q, h, v)
    if left == -math.inf or down == -math.inf or up == math.inf or right == math.inf:
        print("Nu exista dreptunghi")
    else:
        print((right-left)*(up-down))
