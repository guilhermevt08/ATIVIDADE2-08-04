import os

# Função sem parâmetros e sem retorno
def logo():
    os.system('cls')
    print("========")
    print(" SENAI")
    print("========")

# Função com parâmetros e sem retorno
def somar (a, b):
    return a + b

def subtrair (a, b):
    return a - b

#Função com parâmetros e com retorno
def multiplicar (a, b):
    multiplicacao = a * b
    print(f"Multiplicação: {multiplicacao}")



logo()
print("= Solicitando dados =")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = somar(n1, n2)
subtracao = subtrair(n1, n2)

logo()
print("= Exibindo dados =")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
multiplicar(n1, n2)