import pytest


def test_get_entries_no_filter_returns_all(client):
    res = client.get('/api/entries')
    assert res.status_code == 200
    body = res.get_json()
    assert isinstance(body, list)
    assert len(body) == 12


def test_get_entries_gate_filter(client):
    res = client.get('/api/entries?gate=C')
    assert res.status_code == 200
    body = res.get_json()
    assert len(body) == 3
    assert all(e['gate'] == 'C' for e in body)


def test_get_entries_unmatched_gate_is_empty(client):
    res = client.get('/api/entries?gate=Z')
    assert res.status_code == 200
    assert res.get_json() == []


def test_get_entries_returns_500_on_data_layer_error(client, monkeypatch):
    import data_layer

    def boom():
        raise RuntimeError("database unavailable")

    monkeypatch.setattr(data_layer, 'get_all_entries', boom)
    res = client.get('/api/entries')
    assert res.status_code == 500
    body = res.get_json()
    assert 'error' in body


def test_get_entries_health(client):
    res = client.get('/api/health')
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_app_does_not_import_sqlite3():
    import ast
    import inspect
    import app as app_module
    tree = ast.parse(inspect.getsource(app_module))
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported.add(node.module)
    assert 'sqlite3' not in imported, f"app.py must not import sqlite3, got {imported}"
