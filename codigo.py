import random

##Funçoes Principais 
def Roleta():
    return random.randint(1,6)
def MoverJogador(posicao,casas):
    posicao=posicao+casas
    return posicao

def Dado (nJogador,roleta):
   global posJogador1,posJogador2
   if nJogador==1:
       if roleta==1:
          print("O número sorteado pelo dado foi 1, o jogador 1 agora está na posição: ",posJogador1)
          return MoverJogador(posJogador1,1)
        
       if roleta ==3:
           print("O número sorteado pelo dado foi 3, o jogador 1 agora está na posição: ",posJogador1)
           return MoverJogador(posJogador1,-1)
       if roleta==6:
           print("O número sorteado pelo dado foi 6! o Jogador 1 Perdeu uma rodada!")
           

   if nJogador==2:
       if roleta==1:
          print("O número sorteado pelo dado foi 1, o jogador 2 agora está na posição: ",posJogador1)
          return MoverJogador(posJogador2,1)
       if roleta ==3:
           print("O número sorteado pelo dado foi 3, o jogador 2 agora está na posição: ",posJogador1)
           return MoverJogador(posJogador2,-1)
       if roleta==6:
           print("O númetro sorteado pelo dado foi 6! o Jogador 2 Perdeu uma rodada!")
       
       
def Morrer(nJogador):
    global jogador1Vivo,jogador2Vivo
    print("Vida do Jogador 1:\nFilhos: ",filhosJogador1,"\nCasado:",jogador1Casado,"\nDivorciado",jogador1Divorciado,"\nFormado: ",jogador1Formado,"\nFamoso:",jogador1Famoso,"\nDinheiro:",dinheiroJogador1)
    print()
    print("Vida do Jogador 2:\nFilhos: ",filhosJogador2,"\nCasado:",jogador2Casado,"\nDivorciado",jogador2Divorciado,"\nFormado: ",jogador2Formado,"\nFamoso:",jogador2Famoso,"\nDinheiro:",dinheiroJogador2)
    if nJogador==1:
        print("Jogador 2 Venceu! Jogador 1 Morreu")
        jogador1Vivo=False
        return jogador1Vivo
    else:
        print("Jogador 1 Venceu! Jogador 2 Morreu")
        jogador2Vivo=False
        return jogador2Vivo

def DesafioMatematico(roletaDesafio):
    if roletaDesafio==1:
        print("O dado caiu na posição 1")
        Primos()
    elif roletaDesafio==2:
        print("O dado caiu na posição 2")
        Soma()
    elif roletaDesafio==3:
        print("O dado caiu na posição 3")
        Fibo()
    elif roletaDesafio==4:
        print("O dado caiu na posição 4")
        AreaCirculo()
    elif roletaDesafio==5:
        print("O dado caiu na posição 5")
        Fatorial()
    elif roletaDesafio==6:
        print("O dado caiu na posição 6")
        Div()

def Formatura(nJogador,roletaFormou):
    global jogador1Formado,jogador2Formado,cursoJogador1,cursoJogador2
    if nJogador==1:
        if roletaFormou==1:
            print("A roleta caiu no número 1, Você se formou em Direito")
            jogador1Formado=True
            cursoJogador1="Direito"
            return jogador1Formado,cursoJogador1
        elif roletaFormou==2:
            print("A roleta caiu no número 2, Você se formou em Medicina")
            jogador1Formado=True
            cursoJogador1="Medicina"
            return jogador1Formado,cursoJogador1
        elif roletaFormou==3:
            print("A roleta caiu no número 3, Você se formou em Jogos digitais")
            jogador1Formado=True
            cursoJogador1="Jogos digitais"
            return jogador1Formado,cursoJogador1
        elif roletaFormou==4:
            print("A roleta caiu no número 4, Digite o curso que você deseja se formar")
            jogador1Formado=True
            cursoJogador1=input("Você se formou em: ")
            return jogador1Formado,cursoJogador1
        elif roletaFormou==5:
            print("A roleta caiu no número 5, Você se formou em Administração")
            jogador1Formado=True
            cursoJogador1="Administração"
            return jogador1Formado,cursoJogador1
        elif roletaFormou==6:
            print("A roleta caiu no número 6, Você se formou em Análise e desenvolvimento de sistemas!")
            jogador1Formado=True
            cursoJogador1="Análise e desenvolvimento de sistemas"
            return jogador1Formado,cursoJogador1
    elif nJogador==2:
        if roletaFormou==1:
            print("A roleta caiu no número 1, Você se formou em Direito")
            jogador2Formado=True
            cursoJogador2="Direito"
            return jogador2Formado,cursoJogador2
        elif roletaFormou==2:
            print("A roleta caiu no número 2, Você se formou em Medicina")
            jogador2Formado=True
            cursoJogador2="Medicina"
            return jogador2Formado,cursoJogador2
        elif roletaFormou==3:
            print("A roleta caiu no número 3, Você se formou em Jogos digitais")
            jogador2Formado=True
            cursoJogador2="Jogos digitais"
            return jogador2Formado,cursoJogador2
        elif roletaFormou==4:
            print("A roleta caiu no número 4, Digite o curso que você deseja se formar")
            jogador2Formado=True
            cursoJogador2=input("Você se formou em: ")
            return jogador2Formado,cursoJogador2
        elif roletaFormou==5:
            print("A roleta caiu no número 5, Você se formou em Administração")
            jogador2Formado=True
            cursoJogador2="Administração"
            return jogador2Formado,cursoJogador2
        elif roletaFormou==6:
            print("A roleta caiu no número 6, Você se formou em Análise e desenvolvimento de sistemas!")
            jogador2Formado=True
            cursoJogador2="Análise e desenvolvimento de sistemas"
            return jogador2Formado,cursoJogador2


def TerFilho(nJogador,roleta):
    global filhosJogador1,filhosJogador2
    if nJogador==1:
        if roleta ==5:
            print("Você teve gêmeos!")
            filhosJogador1=filhosJogador1+2
            return filhosJogador1
        else:
            print("Você teve 1 filho!")
            filhosJogador1=filhosJogador1+1
            return filhosJogador1
    elif nJogador==2:
        if roleta ==5:
            print("Você teve gêmeos!")
            filhosJogador2=filhosJogador2+2
            return filhosJogador2
        else:
            print("Você teve 1 filho!")
            filhosJogador2=filhosJogador2+1
            return filhosJogador2
    return
def Casar(nJogador):
    global jogador1Casado,jogador2Casado
    if nJogador==1:
        jogador1Casado=True
        return jogador1Casado
    elif nJogador==2:
        jogador2Casado=True
        return jogador2Casado
    
def Divorciar(nJogador):
    global jogador1Divorciado,jogador2Divorciado
    if nJogador==1:
        jogador1Casado=False
        jogador1Divorciado=True
        return jogador1Casado,jogador1Divorciado
    elif nJogador==2:
        jogador2Casado=False
        jogador2Divorciado=True
        return jogador2Casado,jogador2Divorciado
    
def Loteria(nJogador,roleta):
    global dinheiroJogador1,dinheiroJogador2
    if nJogador==1:
        if roleta==1:
            print("Você ganhou R$2,50 no Bolão!")
            dinheiroJogador1=dinheiroJogador1+2.50
            return dinheiroJogador1
        elif roleta==2:
            print("Você ganhou R$5.000,00!")
            dinheiroJogador1=dinheiroJogador1+5000
            return dinheiroJogador1
        elif roleta==3:
            print("Você ganhou R$50.000,00!")
            dinheiroJogador1=dinheiroJogador1+50000
            return dinheiroJogador1
        elif roleta==4:
            print("Você ganhou R$500.000,00!")
            dinheiroJogador1=dinheiroJogador1+500000
            return dinheiroJogador1
        elif roleta==5:
            print("Você ganhou R$5.000.000,00!")
            dinheiroJogador1=dinheiroJogador1+5000000
            return dinheiroJogador1
        elif roleta==6:
            print("Você ganhou R$100.000.000,00!")
            dinheiroJogador1=dinheiroJogador1+100000000
            return dinheiroJogador1
    if nJogador==2:
        if roleta==1:
            print("Você ganhou R$2,50 no Bolão!")
            print("Você ganhou R$2,50 no Bolão!")
            dinheiroJogador2 = dinheiroJogador2 + 2.50
            return dinheiroJogador2
        elif roleta == 2:
            print("Você ganhou R$5.000,00!")
            dinheiroJogador2 = dinheiroJogador2 + 5000
            return dinheiroJogador2
        elif roleta == 3:
            print("Você ganhou R$50.000,00!")
            dinheiroJogador2 = dinheiroJogador2 + 50000
            return dinheiroJogador2
        elif roleta == 4:
            print("Você ganhou R$500.000,00!")
            dinheiroJogador2 = dinheiroJogador2 + 500000
            return dinheiroJogador2
        elif roleta == 5:
            print("Você ganhou R$5.000.000,00!")
            dinheiroJogador2 = dinheiroJogador2 + 5000000
            return dinheiroJogador2
        elif roleta == 6:
            print("Você ganhou R$100.000.000,00!")
            dinheiroJogador2 = dinheiroJogador2 + 100000000
            return dinheiroJogador2


def FicarFamoso(nJogador):
    global jogador1Famoso,jogador2Famoso
    if nJogador==1:
        jogador1Famoso=True
        return jogador1Famoso
    if nJogador == 2:
        jogador2Famoso = True
        return jogador2Famoso

def Resetar(nJogador):
    global posJogador1,filhosJogador1,jogador1Casado,jogador1Divorciado,jogador1Formado,cursoJogador1,jogador1Famoso,dinheiroJogador1,jogador1Vivo,posJogador2, filhosJogador2, jogador2Casado, jogador2Divorciado, jogador2Formado, cursoJogador2, jogador2Famoso, dinheiroJogador2, jogador2Vivo
    if nJogador==1:
        posJogador1=0
        filhosJogador1=0
        jogador1Casado = False
        jogador1Divorciado = False
        jogador1Formado = False
        cursoJogador1 = "não se formou"
        jogador1Famoso = False
        dinheiroJogador1=0.0
        jogador1Vivo = True
        return posJogador1,filhosJogador1,jogador1Casado,jogador1Divorciado,jogador1Formado,cursoJogador1,jogador1Famoso,dinheiroJogador1,jogador1Vivo
    if nJogador == 2:
        posJogador2 = 0
        filhosJogador2 = 0
        jogador2Casado = False
        jogador2Divorciado = False
        jogador2Formado = False
        cursoJogador2 = "não se formou"
        jogador2Famoso = False
        dinheiroJogador2 = 0.0
        jogador2Vivo = True
        return posJogador2, filhosJogador2, jogador2Casado, jogador2Divorciado, jogador2Formado, cursoJogador2, jogador2Famoso, dinheiroJogador2, jogador2Vivo


##Funções Secundárias
def Primos():
    print("Números primos até 100:\n")
    for n in range(2,100):
        primo = True
        for i in range(2,int(n/2)+1):
            if n%i ==0:
                primo=False
                break
        if primo==True:
             print(n)

def Soma():
    soma=0
    for n in range(1,11):
        soma=soma+n
    return print("A soma de 1 até 10 é: ",soma)

def Fibo():
    print("Os 10 primeiros números da Sequência de Fibonacci são:\n")
    a, b = 0, 1
    for _ in range(10):
        print(a, end=" ")
        a, b = b, a + b

def AreaCirculo():
    calculo = 3.14*(2.5**2)
    return print("A área do círculo é: ",calculo)

def Fatorial():
    resultado=1
    for n in range(1,5+1):
        resultado = n*resultado
    print("O fatorial de 5 é ",resultado)

def Div():
    print("Os 5 primeiros Números divisíveis por 2 e por 5 são:\n")
    count = 0
    num = 1
    while count < 5:
        if num % 2 == 0 and num % 5 == 0:
            print(num)
            count += 1
        num += 1

    

##Dados iniciais
    
posJogador1=0
posJogador2=0

filhosJogador1=0
filhosJogador2=0

jogador1Casado = False
jogador2Casado = False

jogador1Divorciado = False
jogador2Divorciado = False

jogador1Formado = False
jogador2Formado = False

cursoJogador1 = "não se formou"
cursoJogador2 = "não se formou"

jogador1Famoso = False
jogador2Famoso = False

dinheiroJogador1=0.0
dinheiroJogador2=0.0

jogador1Vivo = True
jogador2Vivo = True

##Programa principal########################################
#VEZ DO JOGADOR 1#

while posJogador1<21 and posJogador2<21 and jogador1Vivo==True and jogador2Vivo==True:
    input("Jogador 1, aperte ENTER para girar a roleta")
    roleta = Roleta()
    posJogador1 = MoverJogador(posJogador1,roleta)
    if posJogador1==1:
        print("Jogador 1 está na posição 1!")
        roletaDado = Roleta()
        if roletaDado==1:
            posJogador1=Dado(1,roletaDado)
            
        if roletaDado==3:
            posJogador1=Dado(1,roletaDado)
            
        if roletaDado==6:
            Dado(1,roletaDado)

    elif posJogador1==2:
        print("Jogador 1 está na posição 2!")
        jogador1Vivo=Morrer(1)
        break   

    elif posJogador1==3:
        print("Jogador 1 está na posição 3!")
        roletaDado = Roleta()
        if roletaDado==1:
            posJogador1=Dado(1,roletaDado)
        if roletaDado==3:
            posJogador1=Dado(1,roletaDado)
        if roletaDado==6:
            Dado(1,roletaDado)
    elif posJogador1==4:
        print("Jogador 1 está na posição 4!")
        roletaDesafio = Roleta()
        DesafioMatematico(roletaDesafio)
    elif posJogador1==5:
        print("Jogador 1 está na posição 5!")
        print("Você se formou! Gire a roleta e descubra qual foi sua formação!")
        input("Pressione ENTER para girar a roleta")
        roletaFormou = Roleta()
        jogador1Formado,cursoJogador1=Formatura(1,roletaFormou)
    elif posJogador1==6:
        print("Jogador 1 está na posição 6!")
        print("Você teve filho! Jogue o dado e descubra quantos")
        input("Pressione ENTER para girar o dado")
        roletaFilho = Roleta()
        filhosJogador1=TerFilho(1,roletaFilho)
    elif posJogador1==7:
        print("Jogador 1 está na casa 7!")
        print("Você casou!")
        jogador1Casado=Casar(1)
    elif posJogador1==8:
        print("Jogador 1 está na casa 8!")
        jogador1Vivo=Morrer(1)
        break
    elif posJogador1==9:
        print("Jogador 1 está na casa 9!")
        print("Você teve filho! Jogue o dado e descubra quantos")
        input("Pressione ENTER para girar o dado")
        roletaFilho = Roleta()
        filhosJogador1=TerFilho(1,roletaFilho)
    elif posJogador1==10:
        print("Jogador 1 está na posição 10!")
        roletaDado = Roleta()
        if roletaDado==1:
            posJogador1=Dado(1,roletaDado)
            
        if roletaDado==3:
            posJogador1=Dado(1,roletaDado)
            
        if roletaDado==6:
            Dado(1,roletaDado)
    elif posJogador1==11:
        print("Jogador 1 está na posição 11!")
        roletaDesafio = Roleta()
        DesafioMatematico(roletaDesafio)
    elif posJogador1==12:
        print("Jogador 1 está na casa 12!")
        print("Você se divorciou")
        jogador1Casado,jogador1Divorciado=Divorciar(1)
    elif posJogador1==13:
        print("Jogador 1 está na casa 13!")
        print("Você teve filho! Jogue o dado e descubra quantos")
        input("Pressione ENTER para girar o dado")
        roletaFilho = Roleta()
        filhosJogador1=TerFilho(1,roletaFilho)
    elif posJogador1==14:
        print("Jogador 1 está na casa 14!")
        print("Você ganhou na loteria!")
        input("Pressione ENTER para girar a roleta e descobrir quanto você ganhou!")
        roletaLoteria=Roleta()
        dinheiroJogador1=Loteria(1,roletaLoteria)
    elif posJogador1==15:
        print("Jogador 1 está na casa 15!")
        print("Você ficou famoso!")
        jogador1Famoso=FicarFamoso(1)
    elif posJogador1==16:
        print("Jogador 1 está na posição 16!")
        print("Você casou!")
        jogador1Casado=Casar(1)
    elif posJogador1==17:
        print("Jogador 1 está na posição 17!")
        roletaDado = Roleta()
        if roletaDado==1:
            posJogador1=Dado(1,roletaDado)
            
        if roletaDado==3:
            posJogador1=Dado(1,roletaDado)
            
        if roletaDado==6:
            Dado(1,roletaDado)
    elif posJogador1==18:
        print("Jogador 1 está na casa 18!")
        jogador1Vivo=Morrer(1)
        break
    elif posJogador1==19:
        print("Jogador 1 está na casa 19!")
        roletaDesafio = Roleta()
        DesafioMatematico(roletaDesafio)     
    elif posJogador1==20:
        print("Jogador 1 está na casa 20!")
        print("Máquina do tempo, você voltou para o início e perdeu tudo o que tinha!")
        posJogador1,filhosJogador1,jogador1Casado,jogador1Divorciado,jogador1Formado,cursoJogador1,jogador1Famoso,dinheiroJogador1,jogador1Vivo=Resetar(1)
    elif posJogador1==21:
        print("Fim de Jogo!")

#####VEZ DO JOGADOR 2##########
    
    input("Jogador 2, aperte ENTER para girar a roleta")
    roleta = Roleta()
    posJogador2 = MoverJogador(posJogador2, roleta)
    if posJogador2 == 1:
        print("Jogador 2 está na posição 1!")
        roletaDado = Roleta()
        if roletaDado == 1:
            posJogador2 = Dado(2, roletaDado)
        if roletaDado == 3:
            posJogador2 = Dado(2, roletaDado)
        if roletaDado == 6:
            Dado(2, roletaDado)
    elif posJogador2 == 2:
        print("Jogador 2 está na posição 2!")
        jogador2Vivo = Morrer(2)
        break
    elif posJogador2 == 3:
        print("Jogador 2 está na posição 3!")
        roletaDado = Roleta()
        if roletaDado == 1:
            posJogador2 = Dado(2, roletaDado)
        if roletaDado == 3:
            posJogador2 = Dado(2, roletaDado)
        if roletaDado == 6:
            Dado(2, roletaDado)
    elif posJogador2 == 4:
        print("Jogador 2 está na posição 4!")
        roletaDesafio = Roleta()
        DesafioMatematico(roletaDesafio)
    elif posJogador2 == 5:
        print("Jogador 2 está na posição 5!")
        print("Você se formou! Gire a roleta e descubra qual foi sua formação!")
        input("Pressione ENTER para girar a roleta")
        roletaFormou = Roleta()
        jogador2Formado, cursoJogador2 = Formatura(2, roletaFormou)
    elif posJogador2==6:
        print("Jogador 2 está na posição 6!")
        print("Você teve filho! Jogue o dado e descubra quantos")
        input("Pressione ENTER para girar o dado")
        roletaFilho = Roleta()
        filhosJogador2=TerFilho(2,roletaFilho)
    elif posJogador2==7:
        print("Jogador 2 está na casa 7!")
        print("Você casou!")
        jogador2Casado=Casar(2)
    elif posJogador2==8:
        print("Jogador 2 está na casa 8!")
        jogador2Vivo=Morrer(2)
        break
    elif posJogador2==9:
        print("Jogador 2 está na casa 9!")
        print("Você teve filho! Jogue o dado e descubra quantos")
        input("Pressione ENTER para girar o dado")
        roletaFilho = Roleta()
        filhosJogador2=TerFilho(2,roletaFilho)
    elif posJogador2==10:
        print("Jogador 2 está na posição 10!")
        roletaDado = Roleta()
        if roletaDado==1:
            posJogador2=Dado(2,roletaDado)
                
        if roletaDado==3:
            posJogador2=Dado(2,roletaDado)
                
        if roletaDado==6:
            Dado(2,roletaDado)
    elif posJogador2==11:
        print("Jogador 2 está na posição 11!")
        roletaDesafio = Roleta()
        DesafioMatematico(roletaDesafio)
    elif posJogador2==12:
        print("Jogador 2 está na casa 12!")
        print("Você se divorciou")
        jogador2Casado,jogador2Divorciado=Divorciar(2)
    elif posJogador2==13:
        print("Jogador 2 está na casa 13!")
        print("Você teve filho! Jogue o dado e descubra quantos")
        input("Pressione ENTER para girar o dado")
        roletaFilho = Roleta()
        filhosJogador2=TerFilho(2,roletaFilho)
    elif posJogador2==14:
        print("Jogador 2 está na casa 14!")
        print("Você ganhou na loteria!")
        input("Pressione ENTER para girar a roleta e descobrir quanto você ganhou!")
        roletaLoteria=Roleta()
        dinheiroJogador2=Loteria(2,roletaLoteria)
    elif posJogador2==15:
        print("Jogador 2 está na casa 15!")
        print("Você ficou famoso!")
        jogador2Famoso=FicarFamoso(2)
    elif posJogador2==16:
        print("Jogador 2 está na posição 16!")
        print("Você casou!")
        jogador2Casado=Casar(2)
    elif posJogador2==17:
        print("Jogador 2 está na posição 17!")
        roletaDado = Roleta()
        if roletaDado==1:
            posJogador2=Dado(2,roletaDado)
                
        if roletaDado==3:
            posJogador2=Dado(2,roletaDado)
                
        if roletaDado==6:
            Dado(2,roletaDado)
    elif posJogador2==18:
        print("Jogador 2 está na casa 18!")
        jogador2Vivo=Morrer(2)
        break
    elif posJogador2==19:
        print("Jogador 2 está na casa 19!")
        roletaDesafio = Roleta()
        DesafioMatematico(roletaDesafio)     
    elif posJogador2==20:
        print("Jogador 2 está na casa 20!")
        print("Máquina do tempo, você voltou para o início e perdeu tudo o que tinha!")
        posJogador2,filhosJogador2,jogador2Casado,jogador2Divorciado,jogador2Formado,cursoJogador2,jogador2Famoso,dinheiroJogador2,jogador2Vivo=Resetar(2)
    elif posJogador2==21:
        print("Fim de Jogo!")

#fim de jogo
if jogador1Vivo==False:
    print("Jogador 2 Ganhou!")
elif jogador2Vivo==False:
    print("Jogador 1 Ganhou!")
elif posJogador1==21:
    print("Jogador 1 Ganhou!")
    print("Vida do Jogador 1:\nFilhos: ",filhosJogador1,"\nCasado:",jogador1Casado,"\nDivorciado",jogador1Divorciado,"\nFormado: ",jogador1Formado,"\nFamoso:",jogador1Famoso,"\nDinheiro:",dinheiroJogador1)
    print()
    print("Vida do Jogador 2:\nFilhos: ",filhosJogador2,"\nCasado:",jogador2Casado,"\nDivorciado",jogador2Divorciado,"\nFormado: ",jogador2Formado,"\nFamoso:",jogador2Famoso,"\nDinheiro:",dinheiroJogador2)

elif posJogador2==21:
    print("Jogador 2 Ganhou!")
    print("Vida do Jogador 1:\nFilhos: ",filhosJogador1,"\nCasado:",jogador1Casado,"\nDivorciado",jogador1Divorciado,"\nFormado: ",jogador1Formado,"\nFamoso:",jogador1Famoso,"\nDinheiro:",dinheiroJogador1)
    print()
    print("Vida do Jogador 2:\nFilhos: ",filhosJogador2,"\nCasado:",jogador2Casado,"\nDivorciado",jogador2Divorciado,"\nFormado: ",jogador2Formado,"\nFamoso:",jogador2Famoso,"\nDinheiro:",dinheiroJogador2)