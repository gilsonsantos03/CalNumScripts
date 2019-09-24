def funcao(x):
    return x**3 - 9*x + 3


def metodo_secante(erro,p0,p1,n):
    if abs(funcao(p0)) < erro:
        p = p0
    elif abs(funcao(p1)) < erro or abs(p1-p0)<erro:
        p = p1
    i = 1
    while i < n:
        p2 = p1 - (funcao(p1)/(funcao(p1) - funcao(p0)))*(p1-p0)
        print("iteracao: %d" %i)
        print("raiz aproximada: %f" %p1)
        print("f(x): %f\n" % float(funcao(p1)))
        if abs(funcao(p2)) < erro or abs(p2 - p1) < erro:
            p = p2
            break
        p0 = p1
        p1 = p2
        i += 1
    return p

print(metodo_secante(0.0005,0,1,100))
