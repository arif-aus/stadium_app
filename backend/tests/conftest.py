import importlib
import os
import sqlite3
import tempfile

import pytest

import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import data_layer as data_layer_module


SAMPLE_ROWS = [
    (1, 1, 'A', 12, 'none'),
    (2, 9, 'A', 11, 'bag'),
    (3, 3, 'A', 14, 'backpack'),
    (4, 4, 'A', 14, 'bag'),
    (5, 7, 'B', 13, 'none'),
    (6, 2, 'B', 14, 'bag'),
    (7, 14, 'B', 14, 'tote'),
    (8, 5, 'C', 14, 'bag'),
    (9, 11, 'C', 12, 'none'),
    (10, 16, 'C', 14, 'bag'),
    (11, 8, 'D', 14, 'purse'),
    (12, 13, 'D', 15, 'bag'),
]


@pytest.fixture()
def temp_db(tmp_path):
    db_path = str(tmp_path / 'test_stadium.db')
    conn = sqlite3.connect(db_path)
    conn.executescript(
        """
        CREATE TABLE people (
            id      INTEGER PRIMARY KEY,
            name    TEXT    NOT NULL,
            phone   TEXT    NOT NULL
        );
        CREATE TABLE stadium_entries (
            id          INTEGER PRIMARY KEY,
            person_id   INTEGER NOT NULL,
            gate        TEXT    NOT NULL,
            hour        INTEGER NOT NULL,
            bag         TEXT    NOT NULL,
            FOREIGN KEY (person_id) REFERENCES people(id)
        );
        INSERT INTO stadium_entries (id, person_id, gate, hour, bag) VALUES
            (1, 1, 'A', 12, 'none'),
            (2, 9, 'A', 11, 'bag'),
            (3, 3, 'A', 14, 'backpack'),
            (4, 4, 'A', 14, 'bag'),
            (5, 7, 'B', 13, 'none'),
            (6, 2, 'B', 14, 'bag'),
            (7, 14, 'B', 14, 'tote'),
            (8, 5, 'C', 14, 'bag'),
            (9, 11, 'C', 12, 'none'),
            (10, 16, 'C', 14, 'bag'),
            (11, 8, 'D', 14, 'purse'),
            (12, 13, 'D', 15, 'bag');
        """
    )
    conn.commit()
    conn.close()
    # Point the data layer at the temp DB for this test.
    original = data_layer_module.DB_PATH
    data_layer_module.DB_PATH = db_path
    yield db_path
    data_layer_module.DB_PATH = original


@pytest.fixture()
def client(temp_db):
    import app as app_module
    app_module.app.config['TESTING'] = True
    return app_module.app.test_client()
