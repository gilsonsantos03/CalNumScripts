def Min_Quad_Discreto(grau,X,F):
    y=0
    j=0
    i=0
    l=len(X)
    g1=lambda x: x**j  #usa-se lambda para criar uma função em uma linha só (tipo um def)
    g2=lambda x: x**y
    M=[]
    for y in range(grau,-1,-1):
        M+=[[]]
        for j in range(grau,-1,-1):
            soma=0
            for k in range(0,l):
                soma+=(g1(X[k]))*(g2(X[k]))
            M[i]+=[soma]
        soma = 0
        for k in range(0, l):
            soma += F[k] * g2(X[k])
        M[i] += [soma]
        i+=1
    '''for p in range(0,len(M)):
        print(M[p])'''
    return M

