numero: int = int(input("Digite um número: "))

def conta(num):
    inicial = 0
    for inicial in range(num):
        inicial += 1
        print(inicial)
    
    return inicial

conta(numero)