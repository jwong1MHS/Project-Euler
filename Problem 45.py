tn = 286
pn = 166
hn = 144

def triangle(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

while (triangle(tn) != pentagonal(pn) or pentagonal(pn) != hexagonal(hn)):
    if (triangle(tn) < hexagonal(hn)):
        tn += 1
    elif (pentagonal(pn) < hexagonal(hn)):
        pn += 1
    else:
        hn += 1

print(int(triangle(tn)))
