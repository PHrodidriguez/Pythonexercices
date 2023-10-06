#Como descobrir o fatorial de um numero


numero = int(input("Insira um número: "))
print(20 * "-")

fatorial = 1

if numero < 0:
    print("não exite fatorial para números negativos")
elif numero == 0:
    print(f"O fatorial de {numero} é 1")
else:
    for x in range(1,numero+1):
        fatorial *= x
    print(f"o fatorial de {numero} é {fatorial}")
print(20 * "-")