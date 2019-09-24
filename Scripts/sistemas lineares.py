


matriz= [[3,2,4,1],[1,1,2,2],[4,3,2,3]]

def subst_retroativa(m):
    resultado = []
    n = len(m)
    for i in range(n):
        resultado.append(0) #estamos adicionando a quantidade de Xn's na lista que contem o resultado
    xn = (m[n-1][n])/(m[n-1][n-1])   #ultimo termo
    resultado[n-1] = xn  #o ultimo elemento da lista ja sabemos(xn), logo o inserimos
    for k in range(n-1,0,-1):
        s = 0
        for j in range (k+1,n+1):
            s = s + m[k-1][j-1]*resultado[j-1]
        xk = (m[k-1][n] - s)/(m[k-1][k-1])
        resultado[k-1]=xk
    return resultado
    

def elim_gaussiana(a):
    n = len(a)
    for k in range(1,n):
        for i in range(k+1,n+1):
            m = (a[i-1][k-1])/(a[k-1][k-1])
            a[i-1][k-1] = 0
            for j in range(k+1,n+2):
                a[i-1][j-1] = a[i-1][j-1] - m*(a[k-1][j-1])

    return subst_retroativa(a)

def elim_gaussiana_com_permuta(a):
    n = len(a)
    for i in range(1,n):
        l = []
        for k in range(i,n+1):
            g = a[k-1][i-1]
            if g !=0:
                l.append(k)
        if l == []:
            return "o sistema n tem solucao unica!\n"
        else:
            p = min(l)
        if p != i:
            (a[p-1],a[i-1]) = (a[i-1],a[p-1])
        for j in range(i+1, n+1):    #parte da eliminacao gaussiana
            m = a[j-1][i-1]/a[i-1][i-1]
            a[j-1][i-1] = 0
            for w in range(i+1, n+2):
                a[j-1][w-1] = a[j-1][w-1] - m*(a[i-1][w-1])
        if a[n-1][n-1] == 0:
            return "n existe solucao unica"
    return a

def fatoracao_cholesky(m):
    n = len(m)
    l =[[0.0]*n for i in range (n)]
    for i in range(1,n+1):
        soma = 0
        for j in range(1,i):
            soma = soma + (l[i-1][j-1])**2
        r = m[i-1][i-1] - soma
        if r<0:
            return "a matriz n eh definida positiva"
        l[i-1][i-1] = r**(1/2)
        for k in range(i+1, n+1):
            soma = 0
            for j in range (1,i):
                soma = soma + (l[k-1][j-1])*(l[i-1][j-1])
        l[k-1][i-1]=(m[k-1][i-1]-soma)/(l[i-1][i-1])
    return l

def fatoracao_lu(m):
    n = len(m)
    l = [[0.0]*n for i in range (n)]
    u = [[0.0]*n for i in range (n)]
    for i in range(n):
        l[i][i] = 1.0    #l com diagonal unitaria
    if l[0][0] != 0.0 and m[0][0] != 0.0:
        u[0][0] = m[0][0]/l[0][0]
    elif m[0][0] != 0.0 and u[0][0] != 0.0:
        l[0][0] = m[0][0]/u[0][0]
    else:
        return "eh impossivel a fatoracao"
    for j in range(2,n+1):
        u[0][j-1] = m[0][j-1]/l[0][0]
        l[j-1][0] = m[j-1][0]/u[0][0]
    for i in range(2,n):
        if l[i-1][i-1] != 0.0:
            u[i-1][i-1] = (m[i-1][i-1] - sum(l[i-1][k]*u[k][i-1] for k in range (i)))/l[i-1][i-1]
        elif u[i-1][i-1] != 0.0:
            l[i-1][i-1] = (m[i-1][i-1] - sum(l[i-1][k]*u[k][i-1] for k in range (i)))/u[i-1][i-1]
        else:
            return "eh impossivel a fatoracao"
        for j in range (i+1,n+1):
            u[i-1][j-1] = (m[i-1][j-1] - sum(l[i-1][k]*u[k][j-1] for k in range (i)))/l[i-1][i-1]
            l[j-1][i-1] = (m[j-1][i-1] - sum(l[j-1][k]*u[k][i-1] for k in range (i)))/u[i-1][i-1]
        if l[n-1][n-1] != 0.0:
            u[n-1][n-1] = (m[n-1][n-1] - sum(l[n-1][k]*u[k][n-1] for k in range (i)))/l[n-1][n-1]
        elif u[n-1][n-1] != 0.0:
            l[n-1][n-1] = (m[n-1][n-1] - sum(l[n-1][k]*u[k][n-1] for k in range (i)))/u[n-1][n-1]
    return (l,u)

r = fatoracao_lu(matriz)
for i in r:
    for j in i:
        print(j)
    print("\n")


            
            
