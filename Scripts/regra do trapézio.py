import math

###REGRA DO TRAPÉZIO###

def f(x):
    return math.log(1+2*math.atan(x/2))


def regra_do_trap(a,b,k,f):
    h = (b-a)/(2**k) #amplitude do subintervalo
    s = 0 #variável que será a iteração do ciclo da soma parcial que é parcela na soma da qual resulta a área total

    for i in range(2**(k-1)): #será feito o cálculo da soma parcial que é parcela na soma da qual resulta a área total
        s = s + f(a+h*(i+1))

    c = (h/2)*(f(a) + f(b) + 2*s) #valor aproximado da integral após cada iteração
    e = abs(c - 0.808) #erro cometido
    k = 0

    while e < 1: #calcula a ordem de grandeza do erro para que se façam as truncaturas apropriadas
        k = k+1
        e = e*10
    e = math.trunc(e*10**3)/(10**(k+3))
    c = math.trunc(c*10**k)/(10**k) #truncando o resultado de acordo com o erro
    return c


def regra_trap2(a,b,n):
    h = (b-a)/n
    x= []
    for i in range (a,b,int(h)):
        x.append(i)
    y = f
    I = y(1)
    for i in range(2,n+1):
        I = I + 2*y(i)
    I = (h/2)*(I + y(n+1))
    return I

print(regra_do_trap(0,math.pi/2,1,f))
    































            
