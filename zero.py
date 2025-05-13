import numpy as np
from collections.abc import Callable

def g(x:float) -> float:
    return x**2+1

'''
    Calcula o resultado da derivada da função f(x)
'''
def df(f: Callable[[float], float], x: float, h = 1e-6) -> float:
    return (f(x+h)-f(x))/h # Definição formal da derivada

'''
    Calcula o resultado da segunda derivada da função f(x)
'''
def ddf(f: Callable[[float], float], x: float, h = 1e-6) -> float:
    return (df(f,x+h,h) - df(f,x,h))/h # Definição formal da segunda derivada.

'''
    Calcula o zero da funcao f(x), que esteja dentro do intervalo [a,b], usando o método da bisseção
'''
def bissecao(f: Callable[[float], float], intervalo: tuple[float, float], epsilon=0.01, maximoIteracoes=500) -> float:
    fxk1 = xk1 = xk = 0 # Iniciando todas as variáveis
    a = intervalo[0] # Para melhor visualização, definindo a como o primeiro valor do intervalo 
    b = intervalo[1] # Para melhor visualização, definindo b como o segundo valor do intervalo 

    for i in range(maximoIteracoes): # Repetir a função até atingir o máximo de iterações permitido
        xk1 = (a+b)/2 # xk1 passa a ser o valor no meio de a e b
        fxk1 = f(xk1) # Para evitar processamento redundante, salvar o resultado de f(xk1) numa variável
        
        b = xk1 if f(a)*fxk1 < 0 else b # b = xk1 se f(a) vezes f(xk1) seja negativo
        a = xk1 if f(b)*fxk1 < 0 else a # a = xk1 se f(b) vezes f(xk1) seja negativo

        if abs(xk1 - xk) < epsilon: # Critério de parada
            print(f"Convergiu em {i} iterações")
            return xk1
        xk = xk1 # Passou para o próximo loop, xk1 vira xk

    print("Limite de iterações passado!")
    return xk1

# def newton(f: Callable[[float], float], intervalo: tuple[float, float], epsilon=0.01, maximoIteracoes=500):
#     xk1 = xk = 0
#     a = intervalo[0] # Para melhor visualização, definindo a como o primeiro valor do intervalo 
#     b = intervalo[1] # Para melhor visualização, definindo b como o segundo valor do intervalo 
#     for i in range(maximoIteracoes):
#             # TODO: Terminar o método de Newton-Raphson
#         if abs(xk1 - xk) < epsilon: # Critério de parada
#             print(f"Convergiu em {i} iterações")
#             return xk1
#         xk = xk1 # Passou para o próximo loop, xk1 vira xk
#     print("Limite de iterações passado!")
#     return xk1

def secante(f: Callable[[float], float], intervalo: tuple[float, float], epsilon=0.01, maximoIteracoes=500):
    xk1 = xk = 0
    a = intervalo[0] # Para melhor visualização, definindo a como o primeiro valor do intervalo 
    b = intervalo[1] # Para melhor visualização, definindo b como o segundo valor do intervalo 
    for i in range(maximoIteracoes):
            # TODO: Terminar o método da secante
        if abs(xk1 - xk) < epsilon:  # Critério de parada
            print(f"Convergiu em {i} iterações")
            return xk1
        xk = xk1 # Passou para o próximo loop, xk1 vira xk
    print("Limite de iterações passado!")
    return xk1
    

if __name__ == "__main__":
    def funcao(x: float) -> float:
        return x**2 + np.e**x-7

    x = bissecao(funcao,(1,2),0.01)
    print(x)


