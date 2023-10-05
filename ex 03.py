
#Else e if, Elife

''' 
pedro = input("Qual a idade de Pedro? ")

arthur = input("Qual a idade de Arthur? ")

if float(pedro) > float(arthur):
      print("Pedro é maior que arthur")
else:
    print("Arthur é maior do que pedro")
    '''



#Exrcício
'''
01 - Implemente um programa que receba a idade de uma pessoa e imprima mensagem de
acordo com os critérios:
● Menor de 16 anos: MENOR
● Entre 16 e 18 anos: EMANCIPADO
● Maior de 18 anos: MAIOR
02 - Implemente um programa que receba a idade de um nadador e imprima a sua
categoria seguindo as regras
'''

#Solução

'''
print("""Olá, seja bem vindo(a)!!
para se inscrever no programa de natação forneça sua idade """)
'''

'''
idade = input("Qual sua idade? ")

if float(idade) < 16:
    print("MENOR") 
if float(idade) >= 16:
    print("EMANCIPADO")
if float(idade) >= 18:
     print("MAIOR")
     '''

idade = input("Qual sua idade? ")
idade = float(idade)

if idade >= 5 and idade <= 7 :
    print("Categoria: Infantil A")
elif idade > 7 and idade <= 10:
    print("Categoria: Infantil  B")
if idade > 10 and idade <= 13:
     print("Categoria: Juvenil A")
elif idade >= 14 and idade <= 17:
     print("Categoria: Juvenil B")






 


