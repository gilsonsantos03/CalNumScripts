x = 1.5
g = [1.0,1.3,1.6,1.9,2.2]
f = [0.7651977,0.6200860,0.4554022,0.2818186,0.1103623]

def neville(x,g,f):

    n = len(g)
    Q = []
    for i in range (n):
        Q.append([])
    
    for i in range(n):             
        Q[i].append(f[i])

    for i in range(1,n):
        for j in range(1,i+1):
            Q[i].append((((x - g[i-j]) * Q[i][j-1]) - ((x - g[i]) * Q[i-1][j-1])) / (g[i] - g[i-j]))
    return Q

print(neville(x,g,f))

