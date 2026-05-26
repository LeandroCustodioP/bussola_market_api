# 🧭 Bússola Market API - Arquitetura e Escopo

## 1. Visão Geral
A Bússola Market API é o sistema central (backend) de uma mercearia moderna. Ela atua como o motor invisível que conecta o Ponto de Venda (PDV), leitores de estoque e gestão de clientes, garantindo consistência, segurança e alta performance.

## 2. Stack Tecnológica
- **Linguagem:** Python 3.10+
- **Framework Web:** FastAPI (Assíncrono)
- **Validação e Schemas:** Pydantic (v2)
- **Banco de Dados & ORM:** SQLite (desenvolvimento) com SQLAlchemy (v2)
- **Testes:** Pytest e FastAPI TestClient
- **Servidor:** Uvicorn

## 3. Padrões Arquiteturais
O projeto DEVE utilizar a **Clean Architecture** (Arquitetura Limpa) baseada no padrão estrutural **`src-layout`**, dividindo as responsabilidades nas seguintes camadas:
- `src/core/`: Configurações globais, segurança, exceções e logs.
- `src/db/`: Sessão do banco de dados e mapeamento relacional (Models).
- `src/schemas/`: Validação estrita de entrada e saída (Pydantic).
- `src/api/v1/`: Roteamento e controladores (Endpoints).

## 4. Entidades de Domínio e Relacionamentos (O Core do Negócio)
O banco de dados relacional é composto pelas seguintes entidades primárias, com tipagem estrita:

### 4.1. Produto (Estoque)
- `id` (int, Primary Key, Autoincrement)
- `nome` (str, max 100 chars)
- `codigo_barras` (str, unique, exact 13 chars)
- `preco` (float, maior que 0)
- `quantidade_estoque` (int, maior ou igual a 0)
- `categoria` (str)

### 4.2. Cliente (Fidelidade)
- `id` (int, Primary Key, Autoincrement)
- `nome` (str, max 100 chars)
- `telefone` (str, unique, max 15 chars)
- `pontos_fidelidade` (int, default=0)

### 4.3. Venda (Transação Cabeçalho)
- `id` (int, Primary Key, Autoincrement)
- `cliente_id` (int, opcional, Foreign Key -> Cliente.id)
- `valor_total` (float, maior ou igual a 0)
- `metodo_pagamento` (str, Enum: "PIX", "CARTAO", "DINHEIRO")
- `data_hora` (datetime, default=now)
- *Relacionamento:* 1 Venda possui N ItensVenda.

### 4.4. ItemVenda (Transação Detalhe - Tabela Associativa)
- `id` (int, Primary Key, Autoincrement)
- `venda_id` (int, Foreign Key -> Venda.id)
- `produto_id` (int, Foreign Key -> Produto.id)
- `quantidade` (int, maior que 0)
- `preco_unitario_congelado` (float, maior que 0) -> *Nota: Grava o preço do produto no momento exato da venda, garantindo a imutabilidade do histórico financeiro.*