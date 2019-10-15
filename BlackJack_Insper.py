#BlackJack_Insper
import random


deck=[2,3,4,5,6,7,8,9,10,11,12,13,14]*4
cartas = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":10,"12":10,"13":10,"14":1}



#Iniciando o jogo

game = True
entrar=input("Este é o BlackJack Insper!!! Deseja entrar na mesa? (s/n): ")
carteira = float(input("Com quanto dinheiro deseja entrar no jogo? Digite o valor: "))
if entrar=="s":
    rodada = 1

    while game == True:

        recebe_valores=[]
        recebe_valores_pc = []

        print("rodada:{0}".format(rodada))
        aposta_l=[]
        aposta= input("Digite o quanto quer apostar: ")

        if aposta=="fim":
            print("Foi bom jogar com você, volte sempre!!!")
            game=False
        else:
            aposta = float(aposta)

        #Feature 1
            while aposta>carteira:
                print("Você não pode apostar mais dinheiro do que tem, aposte um valor adequado")
                aposta = float(input("Digite o quanto quer apostar: "))

            aposta_l.append(aposta)
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
            
            if sum(recebe_valores)==21 and sum(recebe_valores_pc) == 21:
                print("Você empatou com a IA, mais sorte na proxima tentativa!!")
                print("Carteira: {0}".format(carteira))
                print("NOVA RODADA")

            elif sum(recebe_valores_pc)>21:
                print("A IA estourou, você ganhou!!!")
                carteira+=sum(aposta_l)+1.5*sum(aposta_l)
                print("Carteira {0}".format(carteira))

            elif sum(recebe_valores)>21 and sum(recebe_valores_pc)>21:
                print("Você e a IA estouraram, EMPATE!!!")
                carteira+=sum(aposta)
                print("Carteira{0}".format(carteira))

            elif sum(recebe_valores_pc)==21:
                ganho = sum(aposta_l) 
                carteira-=ganho
                print("Sua soma: ",sum(recebe_valores))
                print("Soma pc: ",sum(recebe_valores_pc))
                print("O IA ganhou de você!! Ele alcançou os 21 pontos! Tente novamente")
                print("agora você tem: R${0}".format(carteira))
                

            elif sum(recebe_valores)==21:
                ganho = sum(aposta_l) + 1.5*sum(aposta_l)
                carteira+=ganho
                print("Sua soma: ",sum(recebe_valores))
                print("Soma IA: ",sum(recebe_valores_pc))
                print("Você fez BlackJack, PARABENS!!!!, você ganhou {0}".format(ganho),"agora você tem: R${0}".format(carteira))
            
            elif sum(recebe_valores)>21:
                print("Sua soma: ",sum(recebe_valores))
                print("Soma pc: ",sum(recebe_valores_pc))
                print("Você perdeu! Estourou os 21 pontos, perdeu R${0}".format(aposta))
                carteira-=sum(aposta_l)
                print("Carteira",carteira)
    

            elif sum(recebe_valores) < 21:
                p = input("Você não fez um Blackjack, deseja parar?(sim/nao): ")
                    
                if p=="nao":
                    if sum(recebe_valores)>17 or sum(recebe_valores_pc)>17:
                        if sum(recebe_valores)>sum(recebe_valores_pc):
                            print("Você chegou mais proximo de um BlackJack que a IA, ganhou essa rodada!!!")
                            ganho = aposta*2
                            carteira+=ganho
                            print("Carteira: R${0}".format(carteira))
                        elif sum(recebe_valores_pc)>sum(recebe_valores):
                            print("Perdeu!!! A IA chegou mais proximo de um BlackJack que você, mais sorte na proxima")
                            print("Carteira: R${0}".format(carteira))
                    else:
                        while sum(recebe_valores)<=17 and sum(recebe_valores_pc)<=17:

                            aposta = float(input("Digite o quanto quer apostar: "))         
                            #Feature 1
                            """
                            while aposta>carteira:
                                print("Você não pode apostar mais dinheiro do que tem, aposte um valor adequado")
                                aposta = float(input("Digite o quanto quer apostar: "))
                                

                            aposta_l.append(aposta)
                            carteira-=aposta
                            print("Carteira: R${0} ".format(carteira))

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

                            if sum(recebe_valores)>17 or sum(recebe_valores_pc)>17:

                                if sum(recebe_valores)>sum(recebe_valores_pc):
                                    ganho = 2*sum(aposta_l)
                                    carteira+=ganho
                                    print("Você chegou mais proxímo de um BlackJack que a IA, ganhou!!!")
                                    print("Carteira:{0}".format(carteira))
                                    

                                elif sum(recebe_valores)<sum(recebe_valores_pc):
                                    carteira-=sum(aposta_l)
                                    print ("Voce perdeu essa rodada...!! Agora você possui uma carteira de R${0}".format(carteira))
                                
                elif p=="sim":
                    if sum(recebe_valores)>sum(recebe_valores_pc):
                        print("Você chegou mais próximo que a IA, ganhou!!!")
                        ganho =  sum(aposta_l)
                        carteira+=ganho
                        print("Carteira: R${0}".format(carteira))

                    elif sum(recebe_valores_pc)>sum(recebe_valores):
                        print("Perdeu!!! A IA chegou mais proximo de um BlackJack que você, mais sorte na próxima vez")
                        print("Carteira: R${0}".format(carteira))
            """

            
                

        #Feature 2
            #if carteira<=0:
                #game = False
            
        rodada+=1

else:
    print("Volte quando quiser jogar!!")



            
