#BlackJack_Insper
import random


deck=[2,3,4,5,6,7,8,9,10,11,12,13,14]*4
cartas = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":10,"12":10,"13":10,"14":1}



#Iniciando o jogo
recebe_valores=[]
recebe_valores_pc = []

entrar=input("Este é o BlackJack Insper!!! Deseja entrar na mesa? (s/n): ")
carteira = float(input("Com quanto dinheiro deseja entrar no jogo? Digite o valor: "))
if entrar=="s":

    while carteira>=0:
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
        print (recebe_valores)
        
        if sum(recebe_valores) and sum(recebe_valores_pc) == 21:
            print("empate")

        elif sum(recebe_valores)==21:
            ganho = aposta + 1.5*aposta
            carteira+=ganho
            print("Sua soma: ",sum(recebe_valores))
            print("Soma pc: ",sum(recebe_valores_pc))
            print("Você fez BlackJack, PARABENS!!!!, você ganhou {0}".format(ganho),"agora você tem: R${0}".format(carteira))
            break

        elif sum(recebe_valores_pc)==21:
            ganho = aposta 
            carteira-=ganho
            print("Sua soma: ",sum(recebe_valores))
            print("Soma pc: ",sum(recebe_valores_pc))
            print("O IA ganhou de você!! Ele alcançou os 21 pontos! Tente novamente")
            print("agora você tem: R${0}".format(carteira))
            break

        elif sum(recebe_valores) < 21:
            p = str(input("Você não fez um Blackjack, deseja parar?(sim/nao): "))
                
            if p=="sim":
                if sum(recebe_valores)>sum(recebe_valores_pc):
                    ganho = 2*aposta
                    carteira+=ganho
                    print ("Parabens, voce ganhou a rodada! Voce ganhou R${0}!! Agora possui uma carteira de R${1}".format(ganho,carteira))
                    break
                elif sum(recebe_valores)<sum(recebe_valores_pc):
                    carteira-=aposta
                    print ("Voce perdeu essa rodada...!! Agora você possui uma carteira de R${0}".format(carteira))
                    break
            else:
                print ("rodada: ")

        elif sum(recebe_valores)>21:
            print("Sua soma: ",sum(recebe_valores))
            print("Soma pc: ",sum(recebe_valores_pc))
            print("Você perdeu! Estourou os 21 pontos, perdeu R${0}".format(aposta))
            carteira-=aposta
            print("Carteira",carteira)
            break
     

else:
    print("Volte quando quiser jogar!!")



            
