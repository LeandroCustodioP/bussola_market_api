# Plano de Implementação: 03_popular_banco

Resumo
- Implementar um script de povoamento (`seed`) idempotente, testes automatizados e documentação mínima para permitir povoar o banco de desenvolvimento e validar comportamento em testes.

Etapas (alto nível)
1. Criar módulo `src/db/seed.py` com função `popular_banco(db: Session)` e CLI `if __name__ == "__main__"` para execução direta.

2. Implementar lógica de inserção idempotente:
   - Para `produtos`: inserir quando `codigo_barras` não existir.
   - Para `clientes`: inserir quando `telefone` não existir.

3. Garantir transação atômica envolvendo todas as inserções usando `Session.begin()`.

4. Adicionar logging das etapas relevantes.

5. Escrever testes `test_seed.py` usando `pytest` e banco em memória (`sqlite:///:memory:`) que verifiquem:
   - Caminho feliz (registros criados conforme spec).
   - Idempotência (executar duas vezes não duplica).
   - Validação de restrições (ex: produto com preço negativo é rejeitado ou não inserido).

6. Atualizar README (seção de como popular o banco) — opcional se `skills/atualizar_readme.md` determinar ser necessário.
Dependências e Considerações
- Reusar `src/db/database.py` e `src/db/models.py` para obter `Base`, `get_db()` e modelos existentes.
- Não criar novas tabelas — apenas inserir dados nas existentes.
- Seguir padrão de tipagem e mensagens em português.
Critério de Pronto (Definition of Done)
- Arquivos adicionados: `src/db/seed.py` (implementação), `test/test_seed.py` (testes).
- `pytest` passa localmente para os testes criados (usando in-memory DB).
- Documentação de execução adicionada ao `README.md` ou `.task`.
