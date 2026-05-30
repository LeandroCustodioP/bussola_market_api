from __future__ import annotations

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from src.db.database import Base
from src.db.models import Cliente, Produto
from src.db.seed import CLIENTES_INICIAIS, PRODUTOS_INICIAIS, popular_banco, validar_produto, validar_cliente


@pytest.fixture(name="engine")
def fixture_engine() -> Engine:
    engine = create_engine("sqlite:///:memory:", future=True)
    Base.metadata.create_all(bind=engine)
    return engine


@pytest.fixture(name="session")
def fixture_session(engine: Engine) -> Session:
    session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
    session = session_local()
    try:
        yield session
    finally:
        session.close()


def test_seed_cria_registros(session: Session) -> None:
    resultado = popular_banco(session)

    assert resultado["produtos_inseridos"] == len(PRODUTOS_INICIAIS)
    assert resultado["clientes_inseridos"] == len(CLIENTES_INICIAIS)

    produtos = session.query(Produto).all()
    clientes = session.query(Cliente).all()

    assert len(produtos) == len(PRODUTOS_INICIAIS)
    assert len(clientes) == len(CLIENTES_INICIAIS)
    assert {produto.codigo_barras for produto in produtos} == {
        item["codigo_barras"] for item in PRODUTOS_INICIAIS
    }
    assert {cliente.telefone for cliente in clientes} == {
        item["telefone"] for item in CLIENTES_INICIAIS
    }


def test_seed_idempotente(session: Session) -> None:
    primeiro = popular_banco(session)
    segundo = popular_banco(session)

    assert primeiro["produtos_inseridos"] == len(PRODUTOS_INICIAIS)
    assert primeiro["clientes_inseridos"] == len(CLIENTES_INICIAIS)

    assert segundo["produtos_inseridos"] == 0
    assert segundo["clientes_inseridos"] == 0

    produtos = session.query(Produto).all()
    clientes = session.query(Cliente).all()

    assert len(produtos) == len(PRODUTOS_INICIAIS)
    assert len(clientes) == len(CLIENTES_INICIAIS)


def test_validar_produto_rejeita_preco_negativo() -> None:
    produto_invalido = {
        "nome": "Teste Negativo",
        "codigo_barras": "7891234000011",
        "preco": -1.0,
        "quantidade_estoque": 10,
        "categoria": "Teste",
    }

    with pytest.raises(ValueError, match="preço do produto deve ser maior que zero"):
        validar_produto(produto_invalido)


def test_validar_cliente_rejeita_telefone_longo() -> None:
    cliente_invalido = {
        "nome": "Cliente Teste",
        "telefone": "1234567890123456",
        "pontos_fidelidade": 0,
    }

    with pytest.raises(ValueError, match="telefone do cliente deve ter até 15 caracteres"):
        validar_cliente(cliente_invalido)
