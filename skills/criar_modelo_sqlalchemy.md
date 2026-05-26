# Habilidade: Criar Modelos SQLAlchemy (v2.0)

Sempre que for solicitado a criar ou atualizar uma tabela do banco de dados (Model), você DEVE seguir este padrão estrito do SQLAlchemy 2.0:

1. **Importações:** Use `Mapped` e `mapped_column` do pacote `sqlalchemy.orm`.
2. **Tipagem:** Todos os atributos da classe devem ter Type Hints explícitos.
3. **Nomenclatura:** O nome da tabela (`__tablename__`) deve ser no plural e em minúsculo (ex: `produtos`, `clientes`).

**Exemplo Perfeito (Molde):**
```python
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float
from src.db.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    preco: Mapped[float] = mapped_column(Float, nullable=False)