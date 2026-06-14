"""Schemas de entrada e saída (Pydantic)."""
from pydantic import BaseModel


# --- Categoria ---
class CategoriaCriar(BaseModel):
    nome: str


class CategoriaResposta(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True  # permite criar o schema a partir do objeto ORM


# ─── TODO (Ryckson): criar os schemas de Transacao ───────────────────────
# TransacaoCriar    -> descricao, valor, tipo, data, categoria_id
# TransacaoResposta -> os campos acima + id  (use from_attributes = True)
#
# Siga o padrão das classes Categoria acima.

# --- Transacao ---
class TransacaoCriar(BaseModel):
    descricao: str
    valor: float
    tipo: str
    data: date
    categoria_id: int


class TransacaoResposta(BaseModel):
    id: int
    descricao: str
    valor: float
    tipo: str
    data: date
    categoria_id: int

    class Config:
        from_attributes = True