# Plan: Banco de Dados

1. **Carregar contexto:** Revisar `.github/copilot-instructions.md`, `.context/arquitetura.md` e `.task/02_banco_de_dados/spec.md` para garantir alinhamento com as regras de tipagem, arquitetura limpa e entidades de negócio.

2. **Definir modelos SQLAlchemy:** Criar os modelos no pacote `src/db/`, incluindo `Produto`, `Cliente`, `Venda` e `ItemVenda` com tipos, constraints e relacionamentos conforme a especificação de domínio.

3. **Configurar sessão e engine:** Implementar a configuração do SQLite em `src/db/`, expondo `engine`, `SessionLocal` e utilitários para criação de sessão. Garantir que a configuração esteja pronta para ser usada pela aplicação e testes.

4. **Organização do pacote `src/db/`:** Garantir a estrutura do pacote com `__init__.py` e módulos separados, preservando o padrão `src-layout` e facilitando a importação de models e banco.

5. **Verificação de consistência:** Adicionar no `.task/02_banco_de_dados/tasks.md` uma tarefa final que compara a implementação com os critérios de aceite do `spec.md`.

6. **Revisão final:** Confirmar que o plano segue as regras de `Type Hints`, `Clean Architecture` e `src-layout` definidas pelo projeto, e que a entrega está pronta para desenvolvimento posterior.
