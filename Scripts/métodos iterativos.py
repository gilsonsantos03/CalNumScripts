matriz = [[10,2,1],[1,5,1],[2,3,10]]
b = [7,-8,6]

xo= [0.7,-1.6,0.6]

def gauss_jacobi(a,b,xo,e,N):
    k =1
    n = len(a)
    x=[]
    for i in range(n):
        x.append(0)
    while k <= N:
        for i in range(1,n+1):
            s = 0
            for j in range (1,n+1):
                if j!=i:
                    s = s + (a[i-1][j-1]*xo[j-1])
            x[i-1] = (b[i-1] - s)/a[i-1][i-1]
        Max = []
        for g in range (1,n+1):
            Max.append(abs(x[g-1] - xo[g-1]))
            if Max[g-1] < e:
                return x
        k = k + 1
        for i in range(1,n+1):
            xo[i-1] = x[i-1]
    return ("max de iteracaoes excedidas",x)




def gauss_seidel(a,b,xo,e,N):
    k = 1
    n = len(a)
    x = []
    for i in range (n):
        x.append(0)
    while k <= N:
        for i in range(1,n+1):
            x[i-1] = (-1*sum(a[i-1][j-1]*x[j-1] for j in range (1,i)) -1*sum(a[i-1][j-1]*xo[j-1] for j in range(i+1, n+1)) + b[i-1])/a[i-1][i-1]
        Max = []
        for g in range (1,n+1):
            Max.append(abs(x[g-1] - xo[g-1]))
            if Max[g-1] < e:
                return x
        k += 1
        for i in range(1,n+1):
            xo[i-1] = x[i-1]
    return ("max de iteracaoes excedidas",x)

print(gauss_seidel(matriz,b,xo,0.05,100))



