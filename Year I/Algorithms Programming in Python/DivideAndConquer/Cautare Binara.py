def divide(v, x, start = 0, finish = None):
    if start == finish:
        return False
    elif start+1 == finish:
        return v[start] == x
    if finish == None:
        return divide(v, x, 0, len(v))
    elif x > v[(finish+start)//2]:
        return divide(v, x, (finish+start)//2, finish)
    elif x < v[(finish+start)//2]:
        return divide(v, x, start, (finish+start)//2)
    else:
        return True


v = [21, 21, 312, 69, 5, 0, -41]
v.sort()
print(divide(v, -41))
print(divide(v, 342351345143))

