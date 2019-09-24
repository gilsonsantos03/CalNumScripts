
g = [1.0,1.3,1.6,1.9,2.2]
f = [0.7651977,0.6200860,0.4554022,0.2818186,0.1103623]

def newton_diferencas_divididas(f,g):
    n = len(g)
    F = []
    for i in range (n):
        F.append([])

    for i in range(n):             
        F[i].append(f[i])

    for i in range(1,n):
        for j in range (1,i+1):
            F[i].append((F[i][j-1] - F[i-1][j-1])/(g[i] - g[i-j]))
    return F

print(newton_diferencas_divididas(f,g))
