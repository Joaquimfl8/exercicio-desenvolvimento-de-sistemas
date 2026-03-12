TABUADA = 10
numero: int = int(input("Digite um número: "))

def tabuada(num):
    inicial = 1

    while inicial != TABUADA + 1:
        print(f"{num} x {inicial} = {num * inicial}")
        inicial += 1

tabuada(numero)