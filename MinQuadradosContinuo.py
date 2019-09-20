# Projeto para a disciplina de Calculo Numerico
# Implementacao do metodo dos minimos quadrados - caso continuo

import sympy as sp
import numpy as np

#- ENTRADA -#

x = sp.symbols('x')
g1 = x**4
g2 = x**2
f = sp.exp(x)
interv = (x, 1, 5)    #intervalo de integracao

#- METODO -#

def MQcont(g1, g2, f, interv):
    """
    :param g1: primeira funcao a ser comparada
    :param g2: segunda funcao a ser comparada
    :param f: funcao a ser avaliada
    :param interv: intervalo de integracao
    :return: os valores de alfa (f(X) = alfa1*g1 + alfa2*g2)
    """
    g = [g1,g2]
    A = [[],[]]
    B = []
    for i in range(2):
        for j in range(2):
            a = g[i]*g[j]
            A[i].append(float(a.integrate(interv).evalf()))
        b = f*g[i]
        B.append(float(b.integrate(interv).evalf()))
    alfa1, alfa2 = np.linalg.solve(A, B)

    return alfa1, alfa2

#- SAIDA -#
result = MQcont(g1, g2, f, interv)
print(result)
alfa1, alfa2 = result

phi = alfa1*g1 + alfa2*g2
resposta = phi.subs(x, 1.38)

print(resposta)

