### 2. Arquivo: `skills/criar_schema_pydantic.md`
**A Metáfora:** É o "Manual da Catraca de Segurança". Ensina a IA a fazer o porteiro da API barrar dados errados com requinte e gerar uma documentação linda.

**Conteúdo para copiar e colar:**
```markdown
# Habilidade: Criar Schemas Pydantic (v2)

Sempre que for criar validações de dados, você DEVE seguir este padrão:

1. **Divisão de Responsabilidades:** Crie sempre pelo menos um schema para Entrada (`Create`) e um para Saída (`Response`). O schema de Response DEVE conter `model_config = {"from_attributes": True}` para ler os dados do SQLAlchemy.
2. **Documentação Rigorosa:** Todo campo deve obrigatoriamente usar a função `Field(...)` contendo `description` e, se apropriado, limites como `min_length`, `gt` (greater than) ou exemplos práticos.

**Exemplo Perfeito (Molde):**
```python
from pydantic import BaseModel, Field

class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100, description="Nome do produto")
    preco: float = Field(..., gt=0, description="Preço unitário. Deve ser maior que zero.")

class ProdutoResponse(ProdutoCreate):
    id: int = Field(..., description="ID gerado automaticamente")

    model_config = {"from_attributes": True}