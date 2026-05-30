# Povoamento Inicial do Banco (Seed)

Este documento descreve como popular o banco de dados com dados iniciais para desenvolvimento e testes.

## Objetivo

Fornecer um conjunto mínimo de dados para permitir testes manuais e iniciar o desenvolvimento da API sem precisar criar produtos e clientes manualmente.

## O que é populado

- 10 produtos básicos com `codigo_barras` único e válido.
- 5 clientes com `telefone` único.

## Como executar

1. Ative seu ambiente virtual.
2. Instale dependências se necessário:

```bash
pip install -r requirements.txt
```

3. Execute o seed:

```bash
python -m src.db.seed
```

> O script também cria as tabelas do banco usando `Base.metadata.create_all()` antes de inserir os registros.

## Comportamento esperado

- Inserções são idempotentes: executar o seed várias vezes não duplica registros.
- O processo usa transação atômica: se algo falhar, nenhuma linha é gravada.
- Regras de validação são aplicadas antes da inserção, incluindo:
  - `codigo_barras` com exatamente 13 caracteres
  - `preco > 0`
  - `quantidade_estoque >= 0`
  - `telefone` com no máximo 15 caracteres

## Testes

O comportamento do seed está coberto por testes no arquivo `test/test_seed.py`.
