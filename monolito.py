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
