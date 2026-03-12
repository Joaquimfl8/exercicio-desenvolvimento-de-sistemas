numero: int = int(input("Digite um número: "))

if (numero % 2):
    print("impar")
else: 
    print("par")

# OU

def isPar(number):
    resto = number % 2
    if resto:
        return "impar"
    else:
        return "par"

print(f"\nO número {numero} é {isPar(numero)}")