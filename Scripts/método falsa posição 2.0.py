import math

def funcao(x):
    return x+1-2*math.sin(math.pi*x)


def metodo_falsa_posicao(a,b,e,n):
    fa = funcao(a)
    fb = funcao(b)
    if abs(b-a)/2 < e:
        p = (a*fb - b*fa)/(fb - fa)
    elif fa*fb>0:
        print("metodo falhou!")
        p = 0 #quando retorna p = 0, eh pq falhou
    else:
        i = 1
        fa = funcao(a)
        while i < n:
            p = (a*funcao(b) - b*fa)/(funcao(b) - fa)
            if abs(funcao(p)) < e:
                p = (a*funcao(b) - b*funcao(a))/(funcao(b) - funcao(a))
                break
            print("iteracao: %d" % i)
            print("raiz aproximada da iteracao: %f" % p)
            print("f(x): %f" % float(funcao(p)))
            print("b-a: %f\n" % ((b-a)/2))
            if fa*funcao(p)>0:
                a = p
            else:
                b = p
            if abs(b-a)/2 < e:
                p = (a*funcao(b) - b*funcao(a))/(funcao(b) - funcao(a))
                break
            i += 1
    return p

print(metodo_falsa_posicao(0,0.5,0.00001,20))

