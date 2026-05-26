# Regras Globais e Diretrizes de Codificação para o Code Assist (AI)

Ao gerar código para o projeto Bússola Market, você (IA) DEVE obedecer estritamente às seguintes regras:

1. **Abordagem Iterativa:** NUNCA gere arquivos gigantes ou o projeto inteiro de uma única vez. Aguarde comandos específicos e iterativos para cada camada (ex: "Crie primeiro os Schemas do Produto").

2. **Arquitetura Base:** O projeto DEVE seguir rigorosamente os princípios da *Clean Architecture* (Arquitetura Limpa) e utilizar o padrão estrutural `src-layout`.

3. **Tipagem Forte:** Todo o código Python (versão 3.10+) deve conter anotações de tipo (`Type Hints`) estritas para variáveis, parâmetros e retornos de funções.

4. **Validação e Documentação Integrada:** Utilize o Pydantic v2 para modelagem de dados. Empregue sempre as ferramentas nativas (`Field`, `summary`, `description`) no FastAPI e no Pydantic para garantir que a documentação gerada no Swagger UI (`/docs`) seja extremamente rica e autodescritiva.

5. **Padrões HTTP e Segurança:**
   - **Respostas:** Siga a semântica correta dos Status HTTP (200 para OK, 201 para Criado, 400 para erro de requisição, 404 para não encontrado, etc).
   - **Isolamento de Dados:** NUNCA exponha dados sensíveis ou colunas internas do banco de dados nos retornos da API. Utilize obrigatoriamente esquemas de saída (`Response Models`) para filtrar e formatar a resposta entregue ao cliente.

6. **Idioma Oficial:** Todo o código fonte (nomes de variáveis, funções, classes), comentários, logs e mensagens de erro DEVEM ser escritos em **Português do Brasil**, garantindo total alinhamento com a equipe local.

7. **Regras de Negócio e Relacionamentos:** Para qualquer dúvida sobre a estrutura das tabelas, atributos, tipos ou relacionamentos entre entidades, consulte primeiramente o arquivo `.context/arquitetura.md`.

8. **Regra de Segurança: Human-in-the-Loop:**
Antes de gerar, modificar ou deletar qualquer arquivo físico (código, estrutura de pastas ou arquivos de configuração), você DEVE parar, descrever o plano de ação e pedir minha confirmação explícita. Não gere código automaticamente sem o meu "OK".