NUMEROS = []

i = 1
for i in range(5):
    numero: int = int(input(f"Digite o número {i+1}: "))
    NUMEROS.append(numero)

def soma(table):
    result = 0
    for i in table:
        result += i
    
    return result

print(soma(NUMEROS))