"""Ponto de entrada da API de Controle Financeiro."""
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import crud, schemas

# Cria as tabelas no banco ao iniciar (simples; suficiente para projeto pequeno).
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Controle Financeiro",
    description="Controle de receitas e despesas com FastAPI.",
    version="0.1.0",
)


@app.get("/health")
def health():
    """Verifica se a API está no ar."""
    return {"status": "ok"}


# --- Categorias (exemplo completo, use como modelo) ---
@app.get("/categorias", response_model=list[schemas.CategoriaResposta])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.listar_categorias(db)


@app.post("/categorias", response_model=schemas.CategoriaResposta)
def criar_categoria(categoria: schemas.CategoriaCriar, db: Session = Depends(get_db)):
    return crud.criar_categoria(db, categoria)


# ─── TODO (Ryckson): endpoints de Transacao ──────────────────────────────
# POST   /transacoes        criar
# GET    /transacoes        listar (filtros opcionais: mes, categoria)
# GET    /transacoes/{id}   buscar uma
# PUT    /transacoes/{id}   atualizar
# DELETE /transacoes/{id}   remover
#
# ─── TODO: endpoint de resumo (o diferencial) ────────────────────────────
# GET /resumo  -> saldo, total por categoria, total por mês
#
# Dica: rode `uvicorn app.main:app --reload` e abra http://localhost:8000/docs
# para testar tudo no Swagger enquanto desenvolve.
