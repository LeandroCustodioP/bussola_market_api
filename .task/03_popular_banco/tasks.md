# Tasks (03_popular_banco)

Lista de tarefas (granular)

1. Escrever `src/db/seed.py` (Implementação) — 3h
   - Criar função `popular_banco(db: Session) -> dict` que retorna resumo de inserções.
   - Implementar inserção idempotente para `produtos` e `clientes`.
   - Usar `Session.begin()` para transação atômica.
   - Adicionar logs informativos.

2. Escrever testes `test/test_seed.py` — 2h
   - `test_seed_cria_registros`: verifica criação inicial.
   - `test_seed_idempotente`: executa `popular_banco` duas vezes e verifica não-duplicação.
   - `test_seed_rejeita_dados_invalidos`: tenta inserir produto com `preco <= 0` e espera comportamento definido (não inserir ou levantar erro de validação).
   - Utilizar banco em memória configurado via `app.dependency_overrides` ou fixture de sessão SQLAlchemy.

3. Adicionar script/CLI de execução local — 0.5h
   - Permitir executar `python -m src.db.seed` para popular o banco de desenvolvimento.

4. Documentar na pasta `docs` em um arquivo especifico e referenciar ele no `README.md`
   - Comando de execução e notas sobre idempotência e testes.

5. Revisão de código e validação com o mantenedor — 0.5h
   - Revisar se os inserts respeitam constraints do `models.py` e se não há vazamento de dados sensíveis.

6. Verificar critérios de aceite — 0.5h
   - Confirmar que todos os critérios de aceitação listados em `spec.md` foram implementados no código, testes e documentação.

Observações
- Se `src/db/models.py` não expuser claramente os campos, abra uma issue antes de implementar alterações estruturais.
- Todos os nomes, mensagens e comentários devem ficar em Português do Brasil.
