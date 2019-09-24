import math


def funcao(x):
    f = 2*x*(math.cos(2*x))-(x+1)**2
    return f

def metodo_bisseccao(a,b,e,n):
    if (b-a)/2 < e:
        p = (a + b)/2
    if funcao(a)*funcao(b)>0:
        print("o metodo falhou!")
        p = 0 #nesse caso nao existe raiz no intervalo, ou o intervalo colocado eh mto grande
    else:
        i = 1
        fa = funcao(a)
        while i < n:
            p = (a + b)/2
            print("iteracao: %d" % i)
            print("raiz aproximada da iteracao: %f" % p)
            print("f(x): %f" % float(funcao(p)))
            print("b-a: %f\n" % ((b-a)/2))
            if fa*funcao(p) > 0:
                a = p
            else:
                b = p
            if (b-a)/2 < e or funcao(p)==0:
                p = (a + b)/2
                break
            i += 1
            
    return p

print(metodo_bisseccao(-3,-2,0.00001,100))



