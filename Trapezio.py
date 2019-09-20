from sympy import *


x = symbols('x')
f = x**2 + 1
a, b = 1, 5


def trapezio(a, b, f, erro):
    
    var = f.free_symbols.pop()  # recebe as variaveis da funcao f
    der2 = f.diff().diff()      # recebe a derivada segunda da funcao

    m = max(der2.subs(var, a), der2.subs(var, b))  # m recebe o maximo valor aplicado na derivada segunda, entre a e b.
    n = (m * pow(b - a, 3) / (12 * erro)) ** (1 / 2)   #quantidade de subdivisoes do intervalo
    passo = (b - a) / n      #tamanho do intervalo


    xi = a
    soma = f.subs(var, xi)   # recebe o valor da funcao no ponto xi

    while xi <= b:
        xi += passo
        soma += 2*f.subs(var,xi)
    soma -= f.subs(var, xi)
    return soma * (passo / 2)


print(trapezio(a, b, f, 0.001))
