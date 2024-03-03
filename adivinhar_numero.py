import random

numero_aleatorio = random.randint(0,100)



print("ADIVINHA O NUMERO DE 0 A 100 !!!")

acertou = 0
while(acertou == 0):
    numero_jogador = int(input("Digite um Numero : "))
    if (numero_jogador > numero_aleatorio):
        print("O Número digitado é maior que o número misterioso!!")
    elif (numero_jogador < numero_aleatorio):
        print ("O Número digitado é menor que o número misterioso!! ")
    else:
        print("PARABENS VOCÊ ACERTOU!!!!!!!!!!!!!!")
        acertou = 1
    