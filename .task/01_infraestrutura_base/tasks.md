# Tarefas: Infraestrutura Base

Esta lista detalha as tarefas atômicas e sequenciais para a criação da estrutura inicial do projeto Bússola Market API.

1.  **Criar Estrutura de Diretórios:** Gerar a árvore de pastas principal (`src`, `src/api/v1`, `src/core`, `src/db`, `src/schemas`, `test/`) conforme o padrão `src-layout`.

2.  **Adicionar Marcadores de Pacote:** Criar arquivos `__init__.py` vazios dentro dos diretórios `src/`, `src/api/`, `src/api/v1/`, `src/core/`, `src/db/` e `src/schemas/` para que sejam reconhecidos como pacotes Python.

3.  **Documentação de Decisão (ADR):** Utilizar a skill `@skills/registrar_adr.md` para registrar a decisão sobre o uso de arquivos `__init__.py` no arquivo `@.context/decisoes_tecnicas.md`.

4.  **Configurar o `.gitignore`:** Criar o arquivo `.gitignore` na raiz do projeto para ignorar arquivos de ambiente virtual, caches, banco de dados local e arquivos `.env`.

5.  **Definir Dependências Iniciais:** Criar o arquivo `requirements.txt` na raiz do projeto e adicionar as bibliotecas `fastapi`, `uvicorn[standard]`, `sqlalchemy`, `pydantic` e `python-dotenv`.

6.  **Criar Arquivo de Ambiente Exemplo:** Criar o arquivo `.env.example` na raiz do projeto com a variável `DATABASE_URL="sqlite:///./bussola.db"` como modelo.

7.  **Criar `README.md` Inicial:** Criar o arquivo `README.md` na raiz do projeto com um título e uma breve descrição.

8.  **Verificar Critérios de Aceite:** Comparar a entrega com os critérios de aceite definidos em `.task/01_infraestrutura_base/spec.md` e confirmar que tudo está conforme.