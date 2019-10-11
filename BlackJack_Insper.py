#BlackJack_Insper
import random
print ("Bem vindo ao Blackjack Insper!")

deck=[2,3,4,5,6,7,8,9,10,11,12,13,14]*4
cartas = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":10,"12":10,"13":10,"14":1}
carteira = float(input("Com quanto dinheiro deseja entrar no jogo? Digite o valor: "))


#Iniciando o jogo
bem_vindo=input("Olá, você está jogando o BlackJack Insper, deseja começar seu jogo?(sim/nao) ")
recebe_valores=[]

while bem_vindo == "sim":
    aposta = float(input("Digite o quanto quer apostar: "))

    primeira_carta = random.randint(2,14)
    #print ("c1",primeira_carta)
    segunda_carta = random.randint(2,14)
    #print("c2",segunda_carta)
    valor_1 = cartas["{0}".format(primeira_carta)]
    recebe_valores.append(valor_1)
    #print(valor_1)
    valor_2 = cartas["{0}".format(segunda_carta)]
    recebe_valores.append(valor_1)
    #print(valor_2)
    print(recebe_valores)

    if sum(recebe_valores)==21:
        ganho = aposta + 1.5*aposta
        carteira+=ganho
        

    


    if aposta=="n":
        break



        
