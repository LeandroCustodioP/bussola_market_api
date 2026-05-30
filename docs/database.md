# Documentação: Banco de Dados

Este documento descreve os modelos de domínio implementados em `src/db/models.py`, os relacionamentos entre eles, as constraints aplicadas e como inicializar o banco para desenvolvimento e testes.

## Modelos

### Produto
- Tabela: `produto`
- Campos:
  - `id` (int, PK, autoincrement)
  - `nome` (str, max 100)
  - `codigo_barras` (str, 13, único)
  - `preco` (float, > 0)
  - `quantidade_estoque` (int, >= 0)
  - `categoria` (str)
- Constraints: `preco > 0`, `quantidade_estoque >= 0`
- Relacionamentos: `itens_venda` (1:N com `ItemVenda`)

### Cliente
- Tabela: `cliente`
- Campos:
  - `id` (int, PK, autoincrement)
  - `nome` (str, max 100)
  - `telefone` (str, max 15, único)
  - `pontos_fidelidade` (int, >= 0)
- Constraints: `pontos_fidelidade >= 0`
- Relacionamentos: `vendas` (1:N com `Venda`)

### Venda
- Tabela: `venda`
- Campos:
  - `id` (int, PK, autoincrement)
  - `cliente_id` (int, FK -> `cliente.id`, opcional)
  - `valor_total` (float, >= 0)
  - `metodo_pagamento` (enum: `PIX`, `CARTAO`, `DINHEIRO`)
  - `data_hora` (datetime, default now)
- Constraints: `valor_total >= 0`
- Relacionamentos: `itens_venda` (1:N com `ItemVenda`), `cliente` (N:1 com `Cliente`)

### ItemVenda
- Tabela: `item_venda`
- Campos:
  - `id` (int, PK, autoincrement)
  - `venda_id` (int, FK -> `venda.id`)
  - `produto_id` (int, FK -> `produto.id`)
  - `quantidade` (int, > 0)
  - `preco_unitario_congelado` (float, > 0)
- Constraints: `quantidade > 0`, `preco_unitario_congelado > 0`
- Relacionamentos: `venda` (N:1), `produto` (N:1)

## Localização do código
- Models: `src/db/models.py`
- Configuração de engine e sessão: `src/db/database.py`
- Utilitários e exportações do pacote: `src/db/__init__.py`

## Como criar as tabelas e executar um teste rápido
1. Ative o ambiente virtual do projeto:

```bash
source .venv/bin/activate
```

2. Instale dependências (se ainda não instaladas):

```bash
pip install -r requirements.txt
```

3. Criar tabelas e executar exemplo de inserção (script de teste):

```bash
python3 src/db/run_db_test.py
```

Saída esperada: mensagens impressas informando a venda criada e seus itens.

## Observações
- O projeto segue o padrão `src-layout` e regras definidas em `.context/arquitetura.md`.
- As constraints de domínio estão aplicadas no nível do schema via `CheckConstraint` para reforçar regras de integridade.
- Mais exemplos de dados (seed) podem ser adicionados em `src/db/` ou em um script `scripts/seed_db.py` se desejado.
