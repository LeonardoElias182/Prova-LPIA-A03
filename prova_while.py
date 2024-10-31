

print ('Tente advinhar o número secreto entre 1 a 10. Você tem 3 tentativas!')

numero_fixo = 7
tentativas = 3

while tentativas > 0:
    chute_usuario = int(input('Digite seu palpite: '))

    if chute_usuario == numero_fixo :
         print('Parabéns, você acertou!')
         break

    else:
        print ('Você errou, tente novamente!')
        tentativas -= 1

else:
   print ('Você não acertou em nenhuma tentativa, tente numa próxima vez!')

