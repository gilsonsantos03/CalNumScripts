#para transformar em diagonal unitaria

def diagonal(m):
    n = len(m)
    for i in range(1,n):
        m[i-1][i-1] = 1.0
    return m

def ldl(a):
    n = len(a)
    l = [[0.0] * n for i in range(n)]
    d = [0.0 for i in range(n)]
    v = [0.0 for i in range(n)]
    L = diagonal(l)
    for i in range(n):
        s = 0
        for j in range(i):
            v[j] = L[i][j]*d[j]
            s += L[i][j]*v[j]
        d[i] = a[i][i] = s
        s1= 0
        for j in range(i+1,n):
            for k in range(i):
                s1 += L[j][k]*v[k]
            L[j][i] = a[j][i] - s1
    return L,d

#para printar a resposta

sol = ldl(a)
for i in sol:
    print(i)
