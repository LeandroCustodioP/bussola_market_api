# Bússola Market API

API RESTful para gerenciar o marketplace Bússola Market.

Este projeto é construído com FastAPI, SQLAlchemy e Pydantic, seguindo a arquitetura limpa e o padrão `src-layout`.

## Sobre

- Estrutura modular em `src/`
- Configuração de ambiente com `.env`
- Dependências definidas no `requirements.txt`

## Uso inicial

1. Crie um ambiente virtual.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Configure `DATABASE_URL` em `.env` ou use o modelo `.env.example`.
4. Execute a aplicação com `uvicorn src.main:app --reload`.

## Povoar banco de dados

Para carregar dados iniciais de desenvolvimento e testes:

```bash
python -m src.db.seed
```

O seed é idempotente e pode ser executado múltiplas vezes sem duplicar registros.

## Documentação

- **Database:** [docs/database.md](docs/database.md) — descrição dos modelos, relacionamentos, constraints e instruções de inicialização do banco de dados.
- **Seed / Povoamento:** [docs/seed.md](docs/seed.md) — instruções para popular o banco de desenvolvimento com dados iniciais.
