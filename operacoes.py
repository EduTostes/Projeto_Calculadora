# Biblioteca para ajudar na criação da função de raiz quadrada
from math import sqrt

# Funções matemáticas que implementa as operações matemáticas

class calculadora:

    def Add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def div(a, b):
        return a / b

    def mult(a, b):
        return a * b

    def pot(a, b):
        return a ** b

    def sqrt(a):
        if a < 0:
            raise ValueError('Erro: Raiz quadrada de número negativo.')
        return sqrt(a)
