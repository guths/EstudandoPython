def partida():
    qnt_pecas=input("Quantas pecas?")
    lmt_pecas_possivel=input("Limite de pecas por jogada?")
    
    if lmt_pecas_possivel>qnt_pecas:
        print("Nao ha como tirar mais  do que {} pecas".format(qnt_pecas))
    else:
        partida()
    if qnt_pecas%lmt_pecas_possivel+1==0:
        print("Voce comeca!")
        auxUsuario=True
        
    else:
        print("Computador comeca!")
    
    if auxUsuario==True:
        for pecas_tiradas in range(qnt_pecas,0,0):
            pecas_tiradas=usuario_escolhe_jogada(qnt_pecas,qnt_pecas)
            qnt_pecas-=pecas_tiradas
            if qnt_pecas==0:
                print("O usuario venceu")
                partida()
            print("Atualmente ha {} pecas".format(qnt_pecas))
            pecas_tiradas=computador_escolhe_jogada(qnt_pecas,lmt_pecas_possivel)
            if qnt_pecas==0:
                print("O computador venceu")
                partida()
                print("Atualmente ha {} pecas".format(qnt_pecas))
            
    else:
        for pecas_tiradas in range(qnt_pecas,0,0):
            pecas_tiradas=computador_escolhe_jogada(qnt_pecas,lmt_pecas_possivel)
            qnt_pecas-=pecas_tiradas
            if qnt_pecas==0:
                print("O computador venceu")
                partida()
                print("Atualmente ha {} pecas".format(qnt_pecas))  
            print("Atualmente ha {} pecas".format(qnt_pecas))
            pecas_tiradas=usuario_escolhe_jogada(qnt_pecas,qnt_pecas)
            if qnt_pecas==0:
                print("O usuario venceu")
                partida()
            print("Atualmente ha {} pecas".format(qnt_pecas))
           
  
def usuario_escolhe_jogada(n,m):
    
    qnt_usuario_remove=int(input("Quantas pecas deseja tirar ?"))

    if n<n-qnt_usuario_remove:
        print("Voce nao pode tirar mais pecas do que ha na mesa")
        qnt_usuario_remove = usuario_escolhe_jogada(n,m)

    if qnt_usuario_remove>m:
        print("Valor invalido ! Voce pode tirar no maximo {} pecas".format(m))
        qnt_usuario_remove = usuario_escolhe_jogada(n,m)

    print("O usuario removeu {} pedras da mesa".format(qnt_usuario_remove))
    return qnt_usuario_remove
        
    
def computador_escolhe_jogada(n,m):
    
    for i in n:
        if n-i%m+1==0:
            qnt_computador_remove=i
    
    print("O computador removeu {} pecas do tabuleiro".format(qnt_computador_remove))
    return qnt_computador_remove



print("Bem-Vindo ao jogo do Nim\n\n")
modo_jogo=int(input("1- Para jogar uma partida isolada\n2- Para jogar um campeonato"))

if modo_jogo==1:
    partida()
          
