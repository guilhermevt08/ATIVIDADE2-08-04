import os
os.system('cls')

def inflacionar_v1(preco):
    if preco >- 100:
        resultado = preco * 1.70
    else:
        resultado = preco * 1.10
    return resultado

def inflacionar_v2(preco):
    if preco >- 100:
        return preco * 1.20
    else:
        return preco * 1.10
def inflacionar_v3(preco):
    return preco * 1.20 if preco >= 100 else preco * 1.10
       
print("= Solicitando dados =")
preco_produto = float(input("Digite o preço do produto: "))

preco_final_v1 = inflacionar_v1(preco_produto)
preco_final_v2 = inflacionar_v2(preco_produto)
preco_final_v3 = inflacionar_v3(preco_produto)

print("\n= Exibindo dados =")
print(f"Preço final - v1: {preco_final_v1}")
print(f"Preço final - v2: {preco_final_v2}")
print(f"Preço final - v3: {preco_final_v3}")
    
