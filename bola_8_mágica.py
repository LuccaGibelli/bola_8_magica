#código criado por Lucca Gibelli
#bola8mágica

import random

pergunta = input('Qual dúvida quer tirar com a Bola 8 Mágica?      ')

numaleatorio = random.randint(1, 9)

if numaleatorio == 1:
    print('Sim - definitivamente')

elif numaleatorio == 2:
    print('Com certeza é assim')
  
elif numaleatorio == 3:
    print('Sem dúvida')

elif numaleatorio == 4:
    print('Resposta confusa, tente novamente')

elif numaleatorio == 5:
    print('Pergunte novamente mais tarde')

elif numaleatorio == 6:
    print('Melhor não te contar agora')

elif numaleatorio == 7:
    print('Minhas fontes dizem que não')

elif numaleatorio == 8:
    print('As perspectivas não são boas')

elif numaleatorio == 9:
    print('Muito duvidoso')

else:
    print('Erro')
