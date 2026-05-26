# Spec: Infraestrutura Base
Objetivo: Preparar o ambiente de desenvolvimento e a estrutura de diretórios seguindo o padrão `src-layout`.

Escopo:
- Criação da árvore de diretórios (`src/`, `src/api/v1`, `src/core`, `src/db`, `src/schemas`, `test/`).
- Definição das dependências iniciais (`requirements.txt`).
- Configuração do Git e arquivos de instrução para o Code Assist (`.github/copilot-instructions.md` ou `.cursorrules`).
- Criação dos arquivos de configuração de ambiente (`.env` e `.gitignore`).

Critérios de Aceite:
- [x] Estrutura de pastas criada conforme o `src-layout`.
- [x] Arquivo `requirements.txt` gerado e pronto para instalação (`pip install`).
- [x] Repositório ignorando arquivos desnecessários (`.gitignore` configurado).
- [x] IA capaz de identificar as regras do projeto através dos arquivos de instrução e `.context/`.