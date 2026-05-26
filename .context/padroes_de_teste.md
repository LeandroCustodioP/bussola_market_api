# 🧪 Padrões de Testes Automatizados

Todas as novas rotas e lógicas de negócio geradas pela IA DEVEM estar acompanhadas de seus respectivos testes automatizados. 

## 1. Ferramentas e Isolamento
- **Framework:** Utilizar estritamente o `pytest` nativo em conjunto com o `TestClient` do FastAPI.
- **Banco de Dados Isolado:** Os testes NUNCA devem tocar no arquivo SQLite de desenvolvimento (`bussola.db`). Utilize a injeção de dependência (`app.dependency_overrides`) para criar um banco de dados temporário em memória (`sqlite:///:memory:`) para cada sessão de teste.

## 2. Cobertura Obrigatória (Caminhos)
Para cada endpoint criado, a IA deve gerar no mínimo dois cenários de teste:
- **Caminho Feliz (Happy Path):** Simula a requisição perfeita. Deve validar se o status de retorno é 200 ou 201 e se os dados salvos no banco estão corretos.
- **Caminho Triste (Sad Path):** Simula falhas e tentativas de abuso. 
  - *Exemplo em Vendas:* Testar o bloqueio de compras quando há estoque negativo.
  - *Exemplo em Produtos:* Testar o retorno de HTTP 422 (Unprocessable Entity) caso o payload seja enviado com um preço negativo.
  - *Exemplo Geral:* Testar requisições em recursos que não existem, garantindo o retorno HTTP 404 (Not Found).