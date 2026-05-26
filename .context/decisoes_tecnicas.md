# 🏛️ Registro de Decisões Técnicas (ADR) - Bússola Market

Este documento registra o histórico das decisões de arquitetura. O agente de IA DEVE respeitar estas decisões e não propor refatorações que contrariem o que está estabelecido aqui.

## ADR 001: Uso de ID Inteiro vs UUID
- **Data:** Maio de 2026
- **Contexto:** Precisávamos definir um padrão de identificação primária para as entidades do banco de dados no início do projeto.
- **Decisão:** Utilizar IDs Inteiros com Autoincremento (Primary Key) em todas as tabelas.
- **Justificativa:** Priorizamos a agilidade no desenvolvimento local e a facilidade de testes manuais via Swagger UI (`/clientes/1` é mais rápido de interagir). A migração para UUID será considerada apenas em um cenário futuro de operação distribuída (offline-first).
- **Consequências:** Simplifica a implementação e o uso inicial, mas exige cuidado ao planejar migrações futuras caso o sistema precise escalar para arquitetura distribuída.

---
### ADR 002: Transação Atômica em Vendas
- **Data:** Maio de 2026
- **Contexto:** O processo de criação de vendas envolve múltiplas operações relacionadas (Venda, ItensVenda e ajuste de estoque).
- **Decisão:** A criação de uma Venda e seus ItensVenda, bem como o desconto de estoque, deve ocorrer em uma única transação no banco de dados.
- **Justificativa:** Se houver um erro de conexão logo após salvar a venda, mas antes de descontar o estoque, o banco de dados deve realizar um `rollback` automático (desfazer tudo). Isso evita dados "fantasmas" ou furos de estoque.
- **Consequências:** Garante consistência e integridade dos dados, mas aumenta a complexidade das operações de persistência e exige tratamento adequado de exceções na camada de banco.

---
### ADR 003: Uso de `__init__.py` em Pacotes Python
- **Data:** Maio de 2026
- **Contexto:** Precisávamos estabelecer uma convenção para garantir que os diretórios do projeto fossem reconhecidos como pacotes Python válidos, especialmente no padrão `src-layout`.
- **Decisão:** Adicionar arquivos `__init__.py` vazios em `src/`, `src/api/`, `src/api/v1/`, `src/core/`, `src/db/` e `src/schemas/`.
- **Justificativa:** Isso garante compatibilidade com importações de pacotes Python e mantém a estrutura do projeto clara e modular durante o desenvolvimento e testes.
- **Consequências:** Os diretórios passam a ser tratados como pacotes Python, facilitando importações internas; o conteúdo dos arquivos permanece vazio para evitar lógica desnecessária.
