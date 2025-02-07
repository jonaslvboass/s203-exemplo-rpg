class SistemaRPG:
    def __init__(self):
        self.usuarios = []  # Armazena mestres e jogadores
        self.mundos = []  # Armazena os mundos criados
        self.paginas = []  # Armazena páginas de conhecimento
        self.personagens = []  # Armazena personagens criados
        self.associacoes_profissoes_culturas = []  # Armazena associações de páginas com profissões e culturas
        self.associacoes_conhecimentos = []  # Armazena associações de páginas com personagens

    # Gerenciamento de contas
    def criar_usuario(self, tipo, login, senha):
        self.usuarios.append({"tipo": tipo, "login": login, "senha": senha})
        print(f"Usuário {login} criado com sucesso!")

    def editar_usuario(self, login, nova_senha):
        for usuario in self.usuarios:
            if usuario["login"] == login:
                usuario["senha"] = nova_senha
                print(f"Usuário {login} atualizado com sucesso!")
                return
        print("Usuário não encontrado!")

    def excluir_usuario(self, login):
        for usuario in self.usuarios:
            if usuario["login"] == login:
                self.usuarios.remove(usuario)
                print(f"Usuário {login} excluído com sucesso!")
                return
        print("Usuário não encontrado!")

    def login(self, login, senha):
        for usuario in self.usuarios:
            if usuario["login"] == login and usuario["senha"] == senha:
                print(f"Login realizado com sucesso para {login}!")
                return usuario
        print("Login falhou! Verifique suas credenciais.")
        return None

    # Gerenciamento de mundos
    def criar_mundo(self, nome, descricao, mestre_login):
        self.mundos.append({"nome": nome, "descricao": descricao, "mestre": mestre_login})
        print(f"Mundo {nome} criado com sucesso!")

    def editar_mundo(self, nome, nova_descricao):
        for mundo in self.mundos:
            if mundo["nome"] == nome:
                mundo["descricao"] = nova_descricao
                print(f"Mundo {nome} atualizado com sucesso!")
                return
        print("Mundo não encontrado!")

    def excluir_mundo(self, nome):
        for mundo in self.mundos:
            if mundo["nome"] == nome:
                self.mundos.remove(mundo)
                print(f"Mundo {nome} excluído com sucesso!")
                return
        print("Mundo não encontrado!")

    # Gerenciamento de páginas
    def criar_pagina(self, titulo, texto, mestre_login):
        self.paginas.append({"titulo": titulo, "texto": texto, "mestre": mestre_login})
        print(f"Página {titulo} criada com sucesso!")

    def editar_pagina(self, titulo, novo_texto):
        for pagina in self.paginas:
            if pagina["titulo"] == titulo:
                pagina["texto"] = novo_texto
                print(f"Página {titulo} atualizada com sucesso!")
                return
        print("Página não encontrada!")

    def excluir_pagina(self, titulo):
        for pagina in self.paginas:
            if pagina["titulo"] == titulo:
                self.paginas.remove(pagina)
                print(f"Página {titulo} excluída com sucesso!")
                return
        print("Página não encontrada!")

    # Gerenciamento de personagens
    def criar_personagem(self, nome, idade, peso, profissao, cultura, antecedente, mundo_nome, jogador_login):
        self.personagens.append({
            "nome": nome,
            "idade": idade,
            "peso": peso,
            "profissao": profissao,
            "cultura": cultura,
            "antecedente": antecedente,
            "mundo": mundo_nome,
            "jogador": jogador_login,
        })
        print(f"Personagem {nome} criado com sucesso!")

    def editar_personagem(self, nome, nova_idade):
        for personagem in self.personagens:
            if personagem["nome"] == nome:
                personagem["idade"] = nova_idade
                print(f"Personagem {nome} atualizado com sucesso!")
                return
        print("Personagem não encontrado!")

    def excluir_personagem(self, nome):
        for personagem in self.personagens:
            if personagem["nome"] == nome:
                self.personagens.remove(personagem)
                print(f"Personagem {nome} excluído com sucesso!")
                return
        print("Personagem não encontrado!")

    # Associações
    def associar_pagina_profissao_cultura(self, titulo_pagina, profissao, cultura):
        self.associacoes_profissoes_culturas.append({"pagina": titulo_pagina, "profissao": profissao, "cultura": cultura})
        print(f"Associação criada para página {titulo_pagina}.")

    def associar_conhecimento_personagem(self, titulo_pagina, personagem_nome):
        self.associacoes_conhecimentos.append({"pagina": titulo_pagina, "personagem": personagem_nome})
        print(f"Página {titulo_pagina} associada ao personagem {personagem_nome}.")

    # Exibição de mundos para jogadores
    def listar_mundos(self, jogador_login):
        print(f"Mundos disponíveis para o jogador {jogador_login}:")
        for mundo in self.mundos:
            print(f"- {mundo['nome']} ({mundo['descricao']})")

    def exibir_menu(self):
        while True:
            print("\n=== Sistema RPG - Menu Principal ===")
            print("1. Gerenciamento de Usuários")
            print("2. Gerenciamento de Mundos")
            print("3. Gerenciamento de Páginas")
            print("4. Gerenciamento de Personagens")
            print("5. Gerenciamento de Associações")
            print("0. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            match opcao:
                case "1":
                    self.menu_usuarios()
                case "2":
                    self.menu_mundos()
                case "3":
                    self.menu_paginas()
                case "4":
                    self.menu_personagens()
                case "5":
                    self.menu_associacoes()
                case "0":
                    print("Saindo do sistema...")
                    break
                case _:
                    print("Opção inválida!")

    def menu_usuarios(self):
        while True:
            print("\n=== Gerenciamento de Usuários ===")
            print("1. Criar usuário")
            print("2. Editar usuário")
            print("3. Excluir usuário")
            print("4. Login")
            print("0. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            match opcao:
                case "1":
                    tipo = input("Tipo (mestre/jogador): ")
                    login = input("Login: ")
                    senha = input("Senha: ")
                    self.criar_usuario(tipo, login, senha)
                case "2":
                    login = input("Login: ")
                    nova_senha = input("Nova senha: ")
                    self.editar_usuario(login, nova_senha)
                case "3":
                    login = input("Login: ")
                    self.excluir_usuario(login)
                case "4":
                    login = input("Login: ")
                    senha = input("Senha: ")
                    self.login(login, senha)
                case "0":
                    break
                case _:
                    print("Opção inválida!")

    def menu_mundos(self):
        while True:
            print("\n=== Gerenciamento de Mundos ===")
            print("1. Criar mundo")
            print("2. Editar mundo")
            print("3. Excluir mundo")
            print("4. Listar mundos")
            print("0. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            match opcao:
                case "1":
                    nome = input("Nome do mundo: ")
                    descricao = input("Descrição: ")
                    mestre_login = input("Login do mestre: ")
                    self.criar_mundo(nome, descricao, mestre_login)
                case "2":
                    nome = input("Nome do mundo: ")
                    nova_descricao = input("Nova descrição: ")
                    self.editar_mundo(nome, nova_descricao)
                case "3":
                    nome = input("Nome do mundo: ")
                    self.excluir_mundo(nome)
                case "4":
                    jogador_login = input("Login do jogador: ")
                    self.listar_mundos(jogador_login)
                case "0":
                    break
                case _:
                    print("Opção inválida!")

    def menu_paginas(self):
        while True:
            print("\n=== Gerenciamento de Páginas ===")
            print("1. Criar página")
            print("2. Editar página")
            print("3. Excluir página")
            print("0. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            match opcao:
                case "1":
                    titulo = input("Título: ")
                    texto = input("Texto: ")
                    mestre_login = input("Login do mestre: ")
                    self.criar_pagina(titulo, texto, mestre_login)
                case "2":
                    titulo = input("Título: ")
                    novo_texto = input("Novo texto: ")
                    self.editar_pagina(titulo, novo_texto)
                case "3":
                    titulo = input("Título: ")
                    self.excluir_pagina(titulo)
                case "0":
                    break
                case _:
                    print("Opção inválida!")

    def menu_personagens(self):
        while True:
            print("\n=== Gerenciamento de Personagens ===")
            print("1. Criar personagem")
            print("2. Editar personagem")
            print("3. Excluir personagem")
            print("0. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            match opcao:
                case "1":
                    nome = input("Nome: ")
                    idade = int(input("Idade: "))
                    peso = float(input("Peso: "))
                    profissao = input("Profissão: ")
                    cultura = input("Cultura: ")
                    antecedente = input("Antecedente: ")
                    mundo_nome = input("Nome do mundo: ")
                    jogador_login = input("Login do jogador: ")
                    self.criar_personagem(nome, idade, peso, profissao, cultura, 
                                       antecedente, mundo_nome, jogador_login)
                case "2":
                    nome = input("Nome: ")
                    nova_idade = int(input("Nova idade: "))
                    self.editar_personagem(nome, nova_idade)
                case "3":
                    nome = input("Nome: ")
                    self.excluir_personagem(nome)
                case "0":
                    break
                case _:
                    print("Opção inválida!")

    def menu_associacoes(self):
        while True:
            print("\n=== Gerenciamento de Associações ===")
            print("1. Associar página a profissão/cultura")
            print("2. Associar conhecimento a personagem")
            print("0. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            match opcao:
                case "1":
                    titulo = input("Título da página: ")
                    profissao = input("Profissão: ")
                    cultura = input("Cultura: ")
                    self.associar_pagina_profissao_cultura(titulo, profissao, cultura)
                case "2":
                    titulo = input("Título da página: ")
                    personagem = input("Nome do personagem: ")
                    self.associar_conhecimento_personagem(titulo, personagem)
                case "0":
                    break
                case _:
                    print("Opção inválida!")

# Example usage:
if __name__ == "__main__":
    sistema = SistemaRPG()
    sistema.exibir_menu()


