
#Do while


palpite = 8
numero = 5

while True:
    print("Qual o número correto?")
    palpite = int(input())
    if palpite == numero:
        print("Parabéns você acertou!!")
        break
    else:
        print("Poxa vida, parece que não foi desta vez!!")
else:
    print("Erro na aplicação")
    print(bool(palpite))        