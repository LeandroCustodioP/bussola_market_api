# 🛒 Regras de Negócio - Bússola Market

Este documento define as regras lógicas e matemáticas que a API deve garantir em todas as operações. Nenhuma rota ou serviço deve violar estas diretrizes.

## 1. Regras de Estoque (Produtos)
- **Bloqueio de Estoque Negativo:** É estritamente proibido aprovar uma venda se a `quantidade_solicitada` for maior que a `quantidade_estoque` atual do produto. A API deve retornar um erro claro (Ex: HTTP 400 - "Estoque insuficiente").
- **Baixa Automática:** Ao finalizar uma venda com sucesso, o sistema deve deduzir imediatamente as quantidades vendidas do estoque dos respectivos produtos.

## 2. Regras de Preço e Histórico Financeiro
- **Congelamento de Preço:** O valor registrado na tabela `ItemVenda` (`preco_unitario_congelado`) DEVE ser uma cópia exata do preço do produto no momento da transação. Isso garante que alterações futuras no cadastro do produto não afetem o cálculo de vendas passadas.
- **Cálculo de Total:** O `valor_total` de uma Venda é estritamente a soma de `(quantidade * preco_unitario_congelado)` de todos os seus itens. A API deve calcular isso no backend, nunca confiando no valor total enviado pelo "Sistema A" (PDV).

## 3. Regras de Fidelidade (Clientes)
- **Acúmulo de Pontos:** A cada R$ 10,00 gastos em uma única venda, o cliente (se identificado no momento da compra) ganha 1 ponto de fidelidade. Valores fracionados não arredondam para cima (ex: R$ 19,90 = 1 ponto).
- **Vendas Anônimas:** A associação de um cliente a uma venda é opcional (`cliente_id` pode ser nulo). Vendas sem cliente não geram pontos para ninguém.