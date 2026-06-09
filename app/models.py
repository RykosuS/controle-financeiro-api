"""Tabelas do banco (SQLAlchemy ORM)."""
from sqlalchemy import Column, Integer, String
from app.database import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)


# ─── TODO (Ryckson): criar o model Transacao ─────────────────────────────
# Campos sugeridos:
#   id           -> Integer, primary_key=True, index=True
#   descricao    -> String, nullable=False
#   valor        -> Float, nullable=False
#   tipo         -> String  ("receita" ou "despesa")
#   data         -> Date
#   categoria_id -> Integer, ForeignKey("categorias.id")
#
# Siga o mesmo padrão da classe Categoria acima.
# Lembre de importar Float, Date e ForeignKey de sqlalchemy.
