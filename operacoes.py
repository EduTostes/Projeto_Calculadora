# Biblioteca para ajudar na criação da função de raiz quadrada
from math import sqrt

# Funções matemáticas que implementa as operações matemáticas

class Calculadora:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def div(a, b):
        if b == 0:
            raise ValueError("Erro: Divisão por zero!")
        return a / b

    @staticmethod
    def mult(a, b):
        return a * b

    @staticmethod
    def pot(a, b):
        return a ** b

    @staticmethod
    def raiz(a):
        if a < 0:
            raise ValueError("Erro: Raiz quadrada de número negativo!")
        return sqrt(a)

