#Ola_Amigo

#Define  VIDA         = 100
#Define  ATAQUE_CURTO = 20
#Define  ATAQUE_LONGO = 20
#Define  DEFESA_CURTA = 5
#Define  DEFESA_LONGA = 5

#personagem [nome, [raça, classe], 
#[vida, ataqueCurto, ataqueLongo, defesaCurta, defesaLonga]]



def escolhaAtributos(nomeAtributo, *atributos):
    print("===================================")
    print("\n##    "+nomeAtributo+"    ##")
    
    contador = 0
    for i in atributos:
        contador += 1
        print (str(contador)+"."+i)
    
    escolha = 0
    while not escolha in range(1, len(atributos)+1):
        escolha = int(input("\nEscolha: "))
    
    print("===================================")

    return atributos[escolha-1]
def recursosPersonagem(raca, classe):
    vida = 100
    ataqueCurto = 20
    ataqueLongo = 20
    defesaCurta = 5
    defesaLonga = 5

    #Recursos das Raças
    if raca == "Elfo": #Elfo
        vida        += 20
        ataqueLongo += 60
        defesaLonga += 20
    elif raca == "Humano": #Humano
        vida        += 20
        ataqueCurto += 30
        ataqueLongo += 20
        defesaCurta += 15
        defesaLonga += 15
    elif raca == "Anão": #Anão
        vida        += 20
        ataqueCurto += 50
        defesaCurta += 30

    #Recursos das Classes
    if classe == "Arqueiro": #Arqueiro
        vida        += 10
        ataqueLongo += 70
        defesaLonga += 20
    elif classe == "Mago": #Mago
        vida        += 20
        ataqueCurto += 25
        ataqueLongo += 25
        defesaCurta += 15
        defesaLonga += 15
    elif classe == "Guerreiro": #Guerreiro
        vida += 30
        ataqueCurto += 35
        ataqueLongo += 10
        defesaCurta += 25

    return [vida, ataqueCurto, ataqueLongo, defesaCurta, defesaLonga]   
def criarPersonagem():
    print("//------CRIAÇÃO DE PERSONAGEM------//")

    #Escolha da Raça
    raca = escolhaAtributos("Raça", "Elfo", "Humano", "Anão")

    #Escolha Classe
    classe = escolhaAtributos("Classe", "Arqueiro", "Mago", "Guerreiro")

    recursos = recursosPersonagem(raca, classe)
    
    return [[raca, classe], recursos]
def cadastraPlayers(i):
    print("####### Jogador "+str(i)+", identifique-se #######\n")
    nome = input("Nome ")
    print ("\n"+nome+" crie seu personagem")
    personagem = criarPersonagem()

    vetorPlayer = [nome, personagem[0], personagem[1]]

    return vetorPlayer
def tela(player1, player2):
    life1 = player1[2][0]
    life2 = player2[2][0]
    barra1 = "="*int(life1/10)
    barra2 = "="*int(life2/10)
    espaco = " "*int(20-life1/10)

    if life1 > 100:
        barra1 = "="*10
        espaco = " "*20
    if life2 > 100:
        barra2 = "="*10

    print ("Life       "+barra1+str(life1)+"hp"+espaco+barra2+str(life2)+"hp")


player1 = cadastraPlayers(1)

player2 = cadastraPlayers(2)

tela(player1, player2)
print (player1)
print (player2)