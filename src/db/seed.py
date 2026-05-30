from __future__ import annotations

import logging
from typing import Any

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .database import Base, engine
from .models import Cliente, Produto

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

PRODUTOS_INICIAIS: list[dict[str, Any]] = [
    {
        "nome": "Arroz Integral 1kg",
        "codigo_barras": "7891234000001",
        "preco": 12.9,
        "quantidade_estoque": 50,
        "categoria": "Alimentos",
    },
    {
        "nome": "Feijão Carioca 1kg",
        "codigo_barras": "7891234000002",
        "preco": 10.5,
        "quantidade_estoque": 40,
        "categoria": "Alimentos",
    },
    {
        "nome": "Açúcar Cristal 1kg",
        "codigo_barras": "7891234000003",
        "preco": 4.8,
        "quantidade_estoque": 60,
        "categoria": "Alimentos",
    },
    {
        "nome": "Café Torrado 500g",
        "codigo_barras": "7891234000004",
        "preco": 14.7,
        "quantidade_estoque": 30,
        "categoria": "Bebidas",
    },
    {
        "nome": "Leite Integral 1L",
        "codigo_barras": "7891234000005",
        "preco": 5.9,
        "quantidade_estoque": 80,
        "categoria": "Laticínios",
    },
    {
        "nome": "Pão de Forma 500g",
        "codigo_barras": "7891234000006",
        "preco": 7.2,
        "quantidade_estoque": 25,
        "categoria": "Padaria",
    },
    {
        "nome": "Óleo de Soja 900ml",
        "codigo_barras": "7891234000007",
        "preco": 9.3,
        "quantidade_estoque": 35,
        "categoria": "Higiene",
    },
    {
        "nome": "Macarrão Espaguete 500g",
        "codigo_barras": "7891234000008",
        "preco": 4.4,
        "quantidade_estoque": 45,
        "categoria": "Alimentos",
    },
    {
        "nome": "Detergente Limpeza 500ml",
        "codigo_barras": "7891234000009",
        "preco": 3.9,
        "quantidade_estoque": 55,
        "categoria": "Limpeza",
    },
    {
        "nome": "Sabonete Glicerinado",
        "codigo_barras": "7891234000010",
        "preco": 2.5,
        "quantidade_estoque": 70,
        "categoria": "Higiene",
    },
]

CLIENTES_INICIAIS: list[dict[str, Any]] = [
    {
        "nome": "Ana Silva",
        "telefone": "11999990001",
        "pontos_fidelidade": 0,
    },
    {
        "nome": "Bruno Costa",
        "telefone": "11999990002",
        "pontos_fidelidade": 0,
    },
    {
        "nome": "Carla Oliveira",
        "telefone": "11999990003",
        "pontos_fidelidade": 0,
    },
    {
        "nome": "Daniel Souza",
        "telefone": "11999990004",
        "pontos_fidelidade": 0,
    },
    {
        "nome": "Eduarda Nunes",
        "telefone": "11999990005",
        "pontos_fidelidade": 0,
    },
]


def validar_produto(produto: dict[str, Any]) -> None:
    if len(produto["codigo_barras"]) != 13:
        raise ValueError("O código de barras deve ter exatamente 13 caracteres.")

    if not produto["nome"] or len(produto["nome"]) > 100:
        raise ValueError("O nome do produto deve ter entre 1 e 100 caracteres.")

    if produto["preco"] <= 0:
        raise ValueError("O preço do produto deve ser maior que zero.")

    if produto["quantidade_estoque"] < 0:
        raise ValueError("A quantidade em estoque não pode ser negativa.")

    if not produto["categoria"] or len(produto["categoria"]) > 100:
        raise ValueError("A categoria do produto deve ter entre 1 e 100 caracteres.")


def validar_cliente(cliente: dict[str, Any]) -> None:
    if not cliente["nome"] or len(cliente["nome"]) > 100:
        raise ValueError("O nome do cliente deve ter entre 1 e 100 caracteres.")

    telefone = cliente["telefone"]
    if not telefone or len(telefone) > 15:
        raise ValueError("O telefone do cliente deve ter até 15 caracteres.")

    if cliente["pontos_fidelidade"] < 0:
        raise ValueError("Os pontos de fidelidade não podem ser negativos.")


def popular_banco(db: Session) -> dict[str, int]:
    logger.info("Iniciando o povoamento do banco de dados.")
    resumo: dict[str, int] = {"produtos_inseridos": 0, "clientes_inseridos": 0}

    with db.begin():
        for produto_data in PRODUTOS_INICIAIS:
            validar_produto(produto_data)
            existente = db.query(Produto).filter_by(codigo_barras=produto_data["codigo_barras"]).first()
            if existente is not None:
                continue
            produto = Produto(**produto_data)
            db.add(produto)
            resumo["produtos_inseridos"] += 1

        for cliente_data in CLIENTES_INICIAIS:
            validar_cliente(cliente_data)
            existente = db.query(Cliente).filter_by(telefone=cliente_data["telefone"]).first()
            if existente is not None:
                continue
            cliente = Cliente(**cliente_data)
            db.add(cliente)
            resumo["clientes_inseridos"] += 1

    logger.info(
        "Povoamento concluído: %s produtos e %s clientes inseridos.",
        resumo["produtos_inseridos"],
        resumo["clientes_inseridos"],
    )

    return resumo


def executar_seed() -> None:
    Base.metadata.create_all(bind=engine)
    from .database import SessionLocal

    session = SessionLocal()
    try:
        resultado = popular_banco(session)
        logger.info("Resumo do seed: %s", resultado)
    except IntegrityError as error:
        session.rollback()
        logger.error("Falha no povoamento devido a violação de integridade: %s", error)
        raise
    except Exception as error:
        session.rollback()
        logger.error("Falha no povoamento: %s", error)
        raise
    finally:
        session.close()


if __name__ == "__main__":
    executar_seed()
