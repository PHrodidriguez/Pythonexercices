#Verificando sinal numérico

numero = int(input('Digite um número: '))

if numero > 0 :
    print("O número é positivo")
elif numero == 0 :
    print("O número é igual a zero")
elif numero < 0 :
    print("O número é negativo")
else:
    print("O número é inválido, verifique e tente novamente.")    

