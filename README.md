# API de Controle Financeiro

API REST para controle de receitas e despesas, construída com FastAPI.
Projeto de portfólio com foco em desenvolvimento back-end.

## Funcionalidades

- CRUD de transações (receitas e despesas)
- CRUD de categorias
- Endpoint de resumo: saldo, total por categoria e total por mês
- Documentação automática (Swagger)

## Stack

- Python 3.12
- FastAPI
- SQLAlchemy (ORM)
- SQLite (banco)
- Pydantic (validação)
- pytest (testes)
- Docker

## Como rodar

### Local (com ambiente virtual)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abra a documentação interativa em: http://localhost:8000/docs

### Com Docker

```bash
docker build -t controle-financeiro-api .
docker run -p 8000:8000 controle-financeiro-api
```

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /health | status da API |
| GET | /categorias | listar categorias |
| POST | /categorias | criar categoria |
| GET | /transacoes | listar transações (filtro por mês/categoria) |
| POST | /transacoes | criar transação |
| GET | /transacoes/{id} | buscar transação |
| PUT | /transacoes/{id} | atualizar transação |
| DELETE | /transacoes/{id} | remover transação |
| GET | /resumo | saldo, total por categoria e por mês |

## Estrutura

```
controle-financeiro-api/
├── app/
│   ├── main.py       # rotas + instância FastAPI
│   ├── database.py   # conexão com o banco
│   ├── models.py     # tabelas (SQLAlchemy)
│   ├── schemas.py    # validação (Pydantic)
│   └── crud.py       # acesso ao banco
├── tests/
│   └── test_health.py
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md
```

## Roadmap

- [x] Setup do projeto (FastAPI + SQLite + Docker)
- [x] CRUD de categorias (exemplo pronto)
- [ ] CRUD de transações
- [ ] Endpoint de resumo (saldo, por categoria, por mês)
- [ ] Testes com pytest
- [ ] (Stretch) Migrar SQLite → PostgreSQL com docker-compose
- [ ] (Stretch) Autenticação JWT
- [ ] (Stretch) Deploy no Render/Railway com link ao vivo do Swagger
