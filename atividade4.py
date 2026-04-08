import os
os.system('cls')

def logo():
    os.system('cls')
    print("========")
    print(" SENAI")
    print("========")

# Função com parâmetros e sem retorno
# Operações em vetores (listas) de mesmo tamanho
def somar(a, b):
    return [x + y for x, y in zip(a, b)]

def subtrair(a, b):
    return [x - y for x, y in zip(a, b)]

# Função com parâmetros e retornos de vetor
# Retorna a multiplicação elemento a elemento
def multiplicar(a, b):
    return [x * y for x, y in zip(a, b)]


def ler_vetor(nome, tamanho):
    print(f"Digite {tamanho} valores para {nome}:")
    vetor = []
    for i in range(tamanho):
        valor = int(input(f"{nome}[{i}]: "))
        vetor.append(valor)
    return vetor


def exibir_vetor(nome, vetor):
    print(f"{nome}: {vetor}")


logo()
print("= Solicitando dados =")
quantidade = int(input("Quantos números terá cada vetor? "))

vetor1 = ler_vetor("vetor1", quantidade)
vetor2 = ler_vetor("vetor2", quantidade)

soma = somar(vetor1, vetor2)
subtracao = subtrair(vetor1, vetor2)
multiplicacao = multiplicar(vetor1, vetor2)

logo()
print("= Exibindo dados =")
exibir_vetor("Vetor 1", vetor1)
exibir_vetor("Vetor 2", vetor2)
exibir_vetor("Soma", soma)
exibir_vetor("Subtração", subtracao)
exibir_vetor("Multiplicação", multiplicacao)
