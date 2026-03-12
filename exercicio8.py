nota: int = int(input("Digite sua nota: "))

if nota >= 7 and nota <= 10:
    print("Aprovado!")
elif nota >= 0 and nota <= 7:
    print("Reprovado!")
else:
    print("Nota inválida")
