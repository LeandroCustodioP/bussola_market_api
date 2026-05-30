from __future__ import annotations

from sqlalchemy import CheckConstraint, Column, DateTime, Enum, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, relationship

from .database import Base


class Produto(Base):
    __tablename__ = "produto"
    __table_args__ = (
        CheckConstraint("preco > 0", name="produto_preco_positivo"),
        CheckConstraint("quantidade_estoque >= 0", name="produto_estoque_nao_negativo"),
    )

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = Column(String(100), nullable=False)
    codigo_barras: Mapped[str] = Column(String(13), unique=True, nullable=False, index=True)
    preco: Mapped[float] = Column(Float, nullable=False)
    quantidade_estoque: Mapped[int] = Column(Integer, nullable=False, default=0)
    categoria: Mapped[str] = Column(String(100), nullable=False)

    itens_venda: Mapped[list["ItemVenda"]] = relationship(
        "ItemVenda",
        back_populates="produto",
        cascade="all, delete-orphan",
    )


class Cliente(Base):
    __tablename__ = "cliente"
    __table_args__ = (
        CheckConstraint("pontos_fidelidade >= 0", name="cliente_pontos_nao_negativos"),
    )

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = Column(String(100), nullable=False)
    telefone: Mapped[str] = Column(String(15), unique=True, nullable=False, index=True)
    pontos_fidelidade: Mapped[int] = Column(Integer, nullable=False, default=0)

    vendas: Mapped[list["Venda"]] = relationship(
        "Venda",
        back_populates="cliente",
        cascade="all, delete-orphan",
    )


class Venda(Base):
    __tablename__ = "venda"
    __table_args__ = (
        CheckConstraint("valor_total >= 0", name="venda_valor_total_nao_negativo"),
    )

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    cliente_id: Mapped[int | None] = Column(Integer, ForeignKey("cliente.id"), nullable=True)
    valor_total: Mapped[float] = Column(Float, nullable=False, default=0.0)
    metodo_pagamento: Mapped[str] = Column(
        Enum("PIX", "CARTAO", "DINHEIRO", name="metodo_pagamento"),
        nullable=False,
    )
    data_hora: Mapped[DateTime] = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    cliente: Mapped["Cliente"] = relationship("Cliente", back_populates="vendas")
    itens_venda: Mapped[list["ItemVenda"]] = relationship(
        "ItemVenda",
        back_populates="venda",
        cascade="all, delete-orphan",
    )


class ItemVenda(Base):
    __tablename__ = "item_venda"
    __table_args__ = (
        CheckConstraint("quantidade > 0", name="item_venda_quantidade_positiva"),
        CheckConstraint("preco_unitario_congelado > 0", name="item_venda_preco_positivo"),
    )

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    venda_id: Mapped[int] = Column(Integer, ForeignKey("venda.id"), nullable=False)
    produto_id: Mapped[int] = Column(Integer, ForeignKey("produto.id"), nullable=False)
    quantidade: Mapped[int] = Column(Integer, nullable=False)
    preco_unitario_congelado: Mapped[float] = Column(Float, nullable=False)

    venda: Mapped["Venda"] = relationship("Venda", back_populates="itens_venda")
    produto: Mapped["Produto"] = relationship("Produto", back_populates="itens_venda")
