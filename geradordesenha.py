# Gerador de senhas



chave = input("Digite a chave para gerar sua senha: ")


senha = " "

for letra in chave:
    if letra in "Aa" : senha = senha + "1"
    elif letra in "Bb" : senha = senha + "W"
    elif letra in "Cc" : senha = senha + "6"
    elif letra in "Dd" : senha = senha + "8"
    elif letra in "Ee" : senha = senha + "4"
    elif letra in "Ff" : senha = senha + "5"
    elif letra in "Tt" : senha = senha + "#"
    elif letra in "Rr" : senha = senha + "$"
    elif letra in "Ss" : senha = senha + "&"
    elif letra in "Oo" : senha = senha + "%"
    elif letra in "Ss" : senha = senha + "*"
    else: senha = senha + letra  
print(senha)

