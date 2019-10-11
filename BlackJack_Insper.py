#BlackJack_Insper
import random
print ("Bem vindo ao Blackjack Insper!")

deck=[2,3,4,5,6,7,8,9,10,11,12,13,14]*4
cartas = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":10,"12":10,"13":10,"14":1}
carteira = float(input("Com quanto dinheiro deseja entrar no jogo? Digite o valor: "))


#Iniciando o jogo
recebe_valores=[]
recebe_valores_pc = []

while carteira>=0:

   # bem_vindo = str(input("Bem-vindo ao BlackJack Insper! Deseja começar?(sim/não)"))

   # if bem_vindo == "nao":
       # break
    
    aposta = float(input("Digite o quanto quer apostar: "))
    carteira-=aposta
    print("Carteira: ",carteira)

    primeira_carta = random.randint(2,14)

    primeira_carta_pc = random.randint(2,14)
    

    segunda_carta = random.randint(2,14)

    segunda_carta_pc = random.randint(2,14)
   

    valor_1 = cartas["{0}".format(primeira_carta)]
    recebe_valores.append(valor_1)

    valor_1_pc = cartas["{0}".format(primeira_carta_pc)]
    recebe_valores_pc.append(valor_1_pc)

    valor_2 = cartas["{0}".format(segunda_carta)]
    recebe_valores.append(valor_1)

    valor_2_pc = cartas["{0}".format(segunda_carta_pc)]
    recebe_valores_pc.append(valor_2_pc)
    

    if sum(recebe_valores)==21:
        ganho = aposta + 1.5*aposta
        carteira+=ganho
        print("Sua soma: ",sum(recebe_valores))
        print("Soma pc: ",sum(recebe_valores_pc))
        print("Você fez BlackJack, PARABENS!!!!, você ganhou {0}".format(ganho),"agora você tem: R${0}".format(carteira))
        break

    elif sum(recebe_valores)!=21:
        p = str(input("Você não fez um Blackjack, deseja parar?(sim/nao): "))
        if p == "sim":
            if sum(recebe_valores)>sum(recebe_valores_pc):
                print("Sua soma: ",sum(recebe_valores))
                print("Soma pc: ",sum(recebe_valores_pc))
                ganho = aposta 
                carteira+=ganho 
                print("PARABENS!!! Você ganhou {0}".format(ganho),"agora você tem: R${0}".format(carteira))
                
        #elif p=="nao":
        elif sum(recebe_valores)>21:
            print("Sua soma: ",sum(recebe_valores))
            print("Soma pc: ",sum(recebe_valores_pc))
            print("Você perdeu! Estourou os 21 pontos, perdeu R${0}".format(aposta))
            carteira-=aposta
            print("Carteira",carteira)

        

    


    if aposta=="n":
        break



        
