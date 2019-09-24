def funcao(x):
    return x**3 - 9*x + 3

def derivada(x):
    return 3*x**2 - 9

def metodo_newton_raphson(erro,p0,n):
    if abs(funcao(p0)) < erro:
        p = p0
    i = 1
    while i < n:
        p1 = p0 - (funcao(p0)/derivada(p0))
        print("iteracao: %d" %i)
        print("raiz aproximada: %f" %p1)
        print("f(x): %f\n" % float(funcao(p1)))
        if abs(funcao(p1)) < erro or abs(p1 - p0) < erro:
            p = p1
            break
        p0 = p1
        i += 1
    return p

print(metodo_newton_raphson(0.0001,0.5,100))
