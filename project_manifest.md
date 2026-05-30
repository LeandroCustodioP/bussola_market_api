# 🧭 Bússola Market API - Visão Geral do Projeto

## 1. O que é este projeto?
A **Bússola Market API** é o sistema central (backend) de uma mercearia moderna. Nosso objetivo é criar uma API rápida, segura e escalável que centralize as operações do Ponto de Venda (PDV), controle de estoque de produtos e gestão de fidelidade de clientes.

## 2. Stack Tecnológica Base
- **Linguagem:** Python 3.10+
- **Framework:** FastAPI
- **Banco de Dados:** SQLite + SQLAlchemy
- **Seed:** Suporte para povoar o banco de dados de desenvolvimento com dados iniciais automatizados

## 3. Mapa de Navegação (Para Desenvolvedores e IA)
Para manter o projeto organizado e a fonte de verdade única, os detalhes específicos estão divididos nos seguintes arquivos:

- 📐 **Arquitetura e Banco de Dados:** Consulte o arquivo `.context/arquitetura.md` para ver as regras de negócio, tabelas, relacionamentos estritos e a explicação da estrutura `src-layout`.
- 🤖 **Regras de Codificação (AI):** Consulte o arquivo `.cursorrules` (ou `.github/copilot-instructions.md`) para entender as regras de tipagem, idioma e padrões HTTP exigidos na geração de código.
- 💻 **Código Fonte:** Toda a lógica da aplicação vive isolada dentro da pasta `src/`.