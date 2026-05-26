# 🔄 Fluxos de Uso e Ordem de Operações

Este documento descreve como os endpoints devem ser desenhados para atender aos processos do mundo real (como o Ponto de Venda ou o Leitor de Estoque).

## Fluxo 1: Realizando uma Venda (Checkout do Caixa)
Para evitar múltiplas chamadas de rede que podem falhar no meio do processo, o fechamento da venda será **atômico** (um único payload robusto).

1. O PDV (Sistema Cliente) agrupa todos os itens bipados no caixa.
2. O PDV envia um único `POST /api/v1/vendas/` contendo um payload JSON com:
   - `cliente_id` (opcional)
   - `metodo_pagamento`
   - Uma lista de `itens`: `[{"produto_id": 1, "quantidade": 2}, {"produto_id": 5, "quantidade": 1}]`
3. A API recebe o payload e realiza as seguintes ações no banco de dados (dentro de uma transação):
   - Valida se há estoque para todos os itens (caso não, cancela tudo e retorna 400).
   - Busca o preço atual de cada produto e calcula o `valor_total`.
   - Salva a `Venda`.
   - Salva os `ItemVenda` congelando o preço.
   - Subtrai o estoque dos produtos.
   - Adiciona os pontos de fidelidade ao cliente (se aplicável).
4. A API retorna HTTP 201 com o recibo detalhado da operação.