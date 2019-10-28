class Perfil():
    'Classe padrao'
    def __init__(self,nome,telefone,empresa):
        self.nome=nome
        self.telefone=telefone
        self.empresa=empresa

    def imprimir(self):
        print('Nome: {}, Telefone: {}, Empresa {}'.format(self.nome,self.telefone,self.empresa))


