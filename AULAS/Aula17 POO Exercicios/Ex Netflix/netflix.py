class Cliente:
    def __init__ (self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos: 
            self.plano = plano
        else:
            print('Plano Inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano inválido')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print('Ver o filme')
        elif self.plano == 'premium':
            print('Ver o filme')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Seu plano não permite ver o filme.')
        else:
            print('Plano inválido')
            
