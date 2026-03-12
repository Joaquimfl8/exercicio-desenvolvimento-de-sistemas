def soma(a, b):
    result = a + b
    return result

def subtracao(a, b):
    result = a - b
    return result

def multiplicacao(a, b):
    result = a * b
    return result

FUNCOES = {
    "soma": soma,
    "subtracao": subtracao,
    "multiplicacao": multiplicacao,
}

a: int = int(input("Insira o valorA: "))
b: int = int(input("Insira o valorB: "))

for i, v in FUNCOES.items():
    print(f"{i}: {v(a, b)}")