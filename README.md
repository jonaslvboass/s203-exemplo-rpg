# Exemplo de Arquitetura de Software

Sistema para gerenciamento de conhecimentos de personagens de RPG.

Os requisitos básicos do sistema são descritos a seguir:

1. O mestre quer criar um conta para acessar o sistema, definindo um login e uma senha. Ele também quer editar e excluir sua conta.
2. O mestre quer cadastrar jogadores informando um login e uma senha para que eles possam acessar o sistema. Ele também quer editar as informações dos jogadores, além de poder excluir essas informações do sistema.
3. O mestre e o jogador querem fazer login para ter acesso ao sistema informando seu login e sua senha.
4. O jogador deve mudar sua senha no primeiro acesso. Ele pode editar e excluir sua conta.
5. O mestre quer cadastrar mundos para as suas campanhas e aventuras, registrando o nome e uma descrição básica para o mundo. Ele também quer editar as informações dos mundos, além de poder excluir essas informações do sistema.
6. O mestre quer cadastrar diferentes páginas para descrever os diferentes conhecimentos a respeito de um determinado mundo, registrando o título e um texto formatado e com imagens sobre essa página. Ele também quer editar as informações das páginas, além de poder excluir essas informações do sistema.
7. O jogador que poder ver a lista de mundos criados pelo seu mestre.
8. O jogador quer criar personagens dentro de um mundo específico, informando seu nome, idade, peso que ele suporta carregar, profissão, cultura, antecedente e data de criação. Ele também quer editar as informações dos seus personagens, além de poder excluir essas informações do sistema.
9. O mestre quer associar para cada página algumas determinadas profissões e culturas de personagens. O objetivo é que os personagens com essas profissões e/ou culturas possam automaticamente acessar as informações descritas por uma determinada página. Ele quer poder editar e excluir essas associações do sistema se necessário.
10. O mestre quer atribuir conhecimentos para personagens. Dessa forma, ele quer associar uma determinada página a um personagem, independente de sua profissão ou cultura. Ele quer poder editar ou excluir essas associações do sistema se necessário.

O arquivo `monolito.py` é uma implementação direta dos requisitos. Entre os diversos problemas desse tipo de implementação, estão:

**Alta complexidade e acoplamento**

- Toda a lógica de negócio está concentrada em uma única classe (SistemaRPG).
- Mudanças em uma funcionalidade podem impactar outras partes do sistema.

**Baixa coesão**

- Métodos que deveriam ser responsabilidade de diferentes classes estão centralizados (métodos de gerenciamento de contas, mundos, páginas e personagens).

**Dificuldade de manutenção**

- Adicionar novas funcionalidades (como permissões avançadas ou auditoria) exige alterações em múltiplos métodos dentro de uma única classe.

**Dificuldade de testar**

- Testar qualquer funcionalidade exige simular o estado de toda a classe, tornando os testes mais complexos.

**Repetição de código**

- Muitos trechos de lógica semelhantes, como loops para buscar itens nas listas, poderiam ser extraídos para métodos auxiliares ou reutilizáveis.

## Melhorando a usabilidade

Apesar do sistema atender os requisitos funcionais, várias mudanças ainda são necessárias para disponibilizar esse sistema para os usuários. Podemos definir os seguintes requisitos não funcionais:

- Os usuários devem conseguir acessar o sistema pelo browser.
- Todos os dados devem ser armazenados para que os usuários possam acessar futuramente.

## Escalando o sistema

Com o aumento do uso do sistema, surgiu a necessidade de melhorar a arquitetura geral do projeto. Entre os novos requisitos estão:

- Mudanças realizadas nos dados do sistema devem refletir imediatamente para todos os usuários.
- Usuários devem receber notificações de novos conehcimentos atribuídos para os seus personagens imediatamente.
- Mestres devem receber notificações de novos personagens criados para checar os dados e atribuir conhecimentos.
