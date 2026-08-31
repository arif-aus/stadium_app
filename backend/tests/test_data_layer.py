import pytest

import data_layer


def test_get_all_entries_returns_all_rows(temp_db):
    entries = data_layer.get_all_entries()
    assert len(entries) == 12


def test_get_all_entries_returns_dicts_with_expected_keys(temp_db):
    entries = data_layer.get_all_entries()
    for entry in entries:
        assert set(entry.keys()) == {'id', 'person_id', 'gate', 'hour', 'bag'}


def test_get_all_entries_ordered_by_hour_desc(temp_db):
    entries = data_layer.get_all_entries()
    hours = [e['hour'] for e in entries]
    assert hours == sorted(hours, reverse=True)


def test_get_entries_by_gate_filters_gate_c(temp_db):
    entries = data_layer.get_entries_by_gate('C')
    assert len(entries) == 3
    assert all(e['gate'] == 'C' for e in entries)


def test_get_entries_by_gate_unmatched_returns_empty(temp_db):
    entries = data_layer.get_entries_by_gate('Z')
    assert entries == []


def test_get_entries_by_gate_returns_dicts_with_expected_keys(temp_db):
    entries = data_layer.get_entries_by_gate('A')
    for entry in entries:
        assert set(entry.keys()) == {'id', 'person_id', 'gate', 'hour', 'bag'}
