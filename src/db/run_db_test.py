from __future__ import annotations

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db import Base, SessionLocal, engine, Produto, Cliente, Venda, ItemVenda


def main() -> None:
    # Cria as tabelas (idempotente)
    Base.metadata.create_all(engine)

    session = SessionLocal()
    try:
        # Criar produto e cliente de exemplo
        produto = Produto(
            nome="Arroz",
            codigo_barras="1234567890123",
            preco=10.5,
            quantidade_estoque=100,
            categoria="Alimentos",
        )
        cliente = Cliente(nome="João Silva", telefone="11999999999", pontos_fidelidade=0)

        session.add_all([produto, cliente])
        session.commit()

        # Criar venda com item
        venda = Venda(cliente_id=cliente.id, valor_total=0.0, metodo_pagamento="DINHEIRO")
        session.add(venda)
        session.flush()

        item = ItemVenda(
            venda_id=venda.id,
            produto_id=produto.id,
            quantidade=2,
            preco_unitario_congelado=produto.preco,
        )
        session.add(item)

        # Atualizar valor total
        venda.valor_total = item.quantidade * item.preco_unitario_congelado
        session.commit()

        # Consultar e exibir
        v = session.query(Venda).filter_by(id=venda.id).one()
        print(f"Venda criada: id={v.id} valor_total={v.valor_total} metodo={v.metodo_pagamento}")
        for it in v.itens_venda:
            print(f" Item: id={it.id} produto_id={it.produto_id} quantidade={it.quantidade} preco_congelado={it.preco_unitario_congelado}")

    except Exception as exc:  # pragma: no cover
        print("Erro durante o teste:", exc)
        raise
    finally:
        session.close()


if __name__ == "__main__":
    main()
