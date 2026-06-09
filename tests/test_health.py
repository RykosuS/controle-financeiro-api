"""Teste de exemplo. Rode com: pytest"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    resposta = client.get("/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}


# ─── TODO (Ryckson): escrever testes para os endpoints de categoria e transacao ───
# Exemplo: criar uma categoria via POST e verificar se ela aparece no GET.
