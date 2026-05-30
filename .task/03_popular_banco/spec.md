# Especificação: 03_popular_banco

Objetivo
- Implementar a funcionalidade de povoamento inicial do banco de dados (seed) para ambiente de desenvolvimento e testes.

Contexto e referências
- Seguir regras de negócio e entidades descritas em `.context/arquitetura.md`.
- Respeitar as Diretrizes de Codificação definidas em `.github/copilot-instructions.md` (tipagem, Pydantic v2, idioma PT-BR, testes automatizados).

Escopo do povoamento
- Entidades a popular inicialmente:
  - `produtos` (id, nome, codigo_barras, preco, quantidade_estoque, categoria)
  - `clientes` (id, nome, telefone, pontos_fidelidade)
  - (Opcional) registros auxiliares mínimos para demonstração: categorias e unidades simples, se necessário.

Critérios de Aceitação
- [x] O script insere pelo menos 10 produtos distintos com `codigo_barras` válidos (13 caracteres) e `preco > 0`.
- [x] O script insere pelo menos 5 clientes com `telefone` único e `pontos_fidelidade = 0` por padrão.
- [x] O povoamento é idempotente: executar o script várias vezes não duplica registros.
- [x] As inserções respeitam restrições de schema: comprimento máximo, unicidade e valores válidos.
- [x] O processo de inserção é atômico, com rollback em caso de falha.
- [x] O sistema registra logs de início, contagem de registros inseridos e rollback em erro.

Não-funcional
- O script deve ser simples de executar localmente (ex: `python -m src.db.seed`).
- Deve ser testável com `pytest` usando banco em memória (`sqlite:///:memory:`).

Restrições
- Não alterar modelos nem esquemas existentes sem aprovação explícita.
- Seguir ADRs registrados (IDs inteiros, transações atômicas).
