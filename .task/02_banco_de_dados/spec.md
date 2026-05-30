# Spec: Banco de Dados
Objetivo: Definir a base relacional do projeto Bússola Market API usando SQLAlchemy e SQLite, garantindo que os modelos reflitam as entidades e relacionamentos definidos na arquitetura.

Escopo:
- Criar modelos SQLAlchemy para as entidades `Produto`, `Cliente`, `Venda` e `ItemVenda`.
- Definir relacionamentos e constraints conforme o arquivo `.context/arquitetura.md`.
- Configurar o banco SQLite e a sessão de acesso em `src/db/`.
- Preservar a arquitetura limpa e o padrão `src-layout` do projeto.

Critérios de Aceite:
- [x] Modelos SQLAlchemy para `Produto`, `Cliente`, `Venda` e `ItemVenda` existem e refletem os campos do domínio.
- [x] Relacionamentos entre `Venda` e `ItemVenda`, `Venda` e `Cliente`, `ItemVenda` e `Produto` estão mapeados corretamente.
- [x] Configuração de sessão/engine do SQLite está implementada em `src/db/` e pronta para uso pela aplicação.
- [x] O arquivo `tasks.md` do work item inclui uma tarefa final de verificação dos critérios de aceite.
- [x] O conteúdo do spec segue as regras de `Type Hints`, `Clean Architecture` e `src-layout` definidas pelo projeto.
