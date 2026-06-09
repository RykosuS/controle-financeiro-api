"""Funções de acesso ao banco (camada CRUD)."""
from sqlalchemy.orm import Session
from app import models, schemas


# --- Categoria (exemplo completo, use como modelo) ---
def listar_categorias(db: Session):
    return db.query(models.Categoria).all()


def criar_categoria(db: Session, categoria: schemas.CategoriaCriar):
    nova = models.Categoria(nome=categoria.nome)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


# ─── TODO (Ryckson): funções de Transacao ────────────────────────────────
# listar_transacoes(db, mes=None, categoria_id=None)
# criar_transacao(db, transacao)
# buscar_transacao(db, transacao_id)
# atualizar_transacao(db, transacao_id, dados)
# remover_transacao(db, transacao_id)
#
# ─── TODO: função de resumo (o diferencial do projeto) ───────────────────
# calcular_resumo(db) -> retornar um dicionário com:
#   - saldo: soma das receitas menos soma das despesas
#   - por_categoria: total gasto/recebido em cada categoria
#   - por_mes: total por mês
# Dica: use db.query(...).all() e some em Python, ou func.sum() do SQLAlchemy.
