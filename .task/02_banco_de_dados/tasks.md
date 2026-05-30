# Tarefas: Banco de Dados

Esta lista detalha as etapas necessárias para implementar a camada de banco de dados da Bússola Market API.

1. **Revisar contexto e spec:** Ler `.github/copilot-instructions.md`, `.context/arquitetura.md` e `.task/02_banco_de_dados/spec.md` para confirmar regras de arquitetura, tipagem e os requisitos do work item.

2. **Criar modelos SQLAlchemy:** Implementar as entidades `Produto`, `Cliente`, `Venda` e `ItemVenda` dentro de `src/db/` com todos os campos, constraints e tipos definidos no domínio.

3. **Mapear relacionamentos:** Garantir os relacionamentos:
   - `Venda` → `Cliente` (opcional)
   - `Venda` → `ItemVenda` (1:N)
   - `ItemVenda` → `Produto`
   utilizando `ForeignKey`, `relationship` e `back_populates` conforme o padrão SQLAlchemy.

4. **Configurar engine e sessão:** Criar a configuração de SQLite em `src/db/`, expondo `engine`, `SessionLocal` e uma função de criação de sessão para uso pela aplicação.

5. **Adicionar pacote `src/db/`:** Garantir que `src/db/` tenha `__init__.py` e esteja organizado para facilitar importação pelos demais módulos do projeto.

6. **Verificação de critérios:** Adicionar uma etapa final que compara a implementação com os critérios de aceite de `.task/02_banco_de_dados/spec.md` e marca o checklist do spec quando cumprido.
