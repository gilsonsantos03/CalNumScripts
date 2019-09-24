def min_quad_continuo(a,b,f,grau):
    y=0
    j=0
    i=0
    g1=lambda x: x**j
    g2=lambda x: x**y
    M=[]
    for y in range(grau,-1,-1):
        M+=[[]]
        for j in range(grau,-1,-1):
            g3=lambda x: g1(x)*g2(x)
            M[i]+=[Regra_dos_Trapezios(a,b,g3)]
        g3=lambda x: f(x)*g2(x)
        M[i] += [Regra_dos_Trapezios(a,b,g3)]
        i+=1
    '''for p in range(0,len(M)):
        print(M[p])'''
    return M

