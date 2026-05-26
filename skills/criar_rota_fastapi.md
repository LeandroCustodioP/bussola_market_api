### 3. Arquivo: `skills/criar_rota_fastapi.md`
**A Metáfora:** É o "Treinamento do Garçom". Ensina a IA a criar as URLs, pegar a requisição do cliente, ir no banco de dados e tratar qualquer erro de forma padronizada.

**Conteúdo para copiar e colar:**
```markdown
# Habilidade: Criar Endpoints FastAPI

Sempre que for criar um novo controlador (rota) no FastAPI, siga estas regras:

1. **Roteamento:** Use `APIRouter(prefix="/...", tags=["..."])`.
2. **Injeção de Dependência:** Injete sempre a sessão do banco usando `db: Session = Depends(get_db)`.
3. **Tratamento de Erros de Negócio:** Se uma busca falhar, levante um `HTTPException(status_code=404)` com mensagem em português.
4. **Blindagem de Exceções Genéricas:** Todo o bloco lógico deve estar dentro de um `try/except Exception` para evitar que a API quebre e vaze detalhes técnicos. Em caso de erro interno, retorne status 500.

**Exemplo Perfeito (Molde):**
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# Importe seus schemas e models aqui

router = APIRouter(prefix="/itens", tags=["Itens"])

@router.get("/{item_id}", response_model=ItemResponse)
def buscar_item(item_id: int, db: Session = Depends(get_db)):
    try:
        item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Item não encontrado no sistema.")
        return item
    except HTTPException:
        raise
    except Exception as e:
        # Aqui no futuro entra o logger
        raise HTTPException(status_code=500, detail="Erro interno no servidor.")