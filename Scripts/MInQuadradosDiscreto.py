# Projeto para a disciplina de Calculo Numerico
# Implementacao do metodo dos minimos quadrados - caso discreto

#- ENTRADAS -#

xi = [-1.0, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1]
yi = [2.05, 1.153, 0.45, 0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05]
x = 0.68

#- METODOS -#

def ResolveSist(A, b):      # Resolve o sistema
    for linha_A, bi in zip(A, b):
        linha_A.append(bi)
    n = len(A)
    for i in range(0, n):
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        for k in range(i, n + 1):
            A[maxRow][k], A[i][k] = A[i][k], A[maxRow][k]

        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i] if A[i][i] != 0 else 0
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i] if A[i][i] != 0 else 0
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x

def soma(Xi, n, Yi=None):
    """
    :param Xi: lista de valores iniciais
    :param n:  grau do polinomio
    :param Yi: lista com o valor da funcao no pontos iniciais
    :return: somatorio de (xi**n) ; se Yi nao for vazio: somatorio de yi*(xi**n)
    """
    if Yi == None:
        return sum(pow(x, n) for x in Xi)
    return sum(y * pow(x, n) for y, x in zip(Yi, Xi))

def MQdisc(xi, yi, n, x, forma = None):
    """
    :param xi: valores iniciais
    :param yi: f(x) correspondente aos valores xi
    :param n: grau do polinomio
    :param x: ponto estudado
    :param forma: forma do polinomio
    :return: aproximacao do ponto estudado
    """

    A = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for j in range(n + 1):
        for i in range(n + 1):
            A[i][j] = soma(xi, i + j)
    b = [soma(xi, i, yi) for i in range(n + 1)]
    a = ResolveSist(A,b)
    resultado = 0
    if forma:
        for i, _bool in enumerate(forma):
            if _bool:
                resultado += a[i] * pow(x,i)
        return resultado
    resultado = sum(a[i] * pow(x, i) for i in range(n + 1))

    return resultado

#- SAIDA -#

p = MQdisc(xi, yi, 4, x, [0, 0, 1,0,1])

print(p)