def viraj(P, Q, R):
    return((Q[1] - P[1]) * (R[0] - Q[0]) - (Q[0] - P[0]) * (R[1] - Q[1]))

def hull(points):
    l = len(points)
    
    if l<3:
        return

    minim = float("inf")
    cel_mai_din_stanga = None
    for point in range(len(points)):
        if points[point][0] < minim:
            minim = points[point][0]
            cel_mai_din_stanga = point
    
    hull = []
    hull.append(points[cel_mai_din_stanga])

    q = 0
    p = cel_mai_din_stanga
    while(True):
        q = (p+1)%l

        for i in range(l):
            P = points[p]
            Q = points[i]
            R = points[q]
            if viraj(P,Q,R)>0:
                q=i

        p = q

        if(len(hull)>2):
            P = points[p]
            Q = hull[len(hull)-1]
            R = hull[len(hull)-2]
            if(abs(viraj(P,Q,R))<0.0000001):
                hull.pop()

        hull.append(points[p])
    
        if(p==cel_mai_din_stanga):
            break
        

    hull.pop()
    return hull

if __name__ == "__main__":
    f = open("coord.in","r")

    points = []
    l = f.readline()
    while(l):
        t = tuple(float(i) for i in l.split())
        points.append(t)
        l = f.readline()

    print(hull(points))
    
    