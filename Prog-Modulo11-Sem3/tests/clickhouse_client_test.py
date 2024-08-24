# Faça os testes dos métodos get_client, execute_sql_script, insert_dataframe do módulo aulaafonse/clickhouse_client.py.

from aulaafonse.clickhouse_client import get_client, execute_sql_script, insert_dataframe
import pandas as pd
from datetime import date
import pytest

def test_get_client():
    client = get_client()
    assert client is not None

def test_execute_sql_script():
    client = execute_sql_script('sql/create_table.sql')
    assert client is not None

def test_insert_dataframe():
    client = get_client()
    actualDate = date.today()
    df = pd.DataFrame({
        'data_ingestao': [actualDate, actualDate, actualDate],
        'dado_linha': ['{"name": "Pikachu", "type": "Electric"}', '{"name": "Charmander", "type": "Fire"}', '{"name": "Squirtle", "type": "Water"}'],
        'tag': ['pokemon', 'pokemon', 'pokemon']
    })
    table_name = 'test_insert_dataframe'
    client.command(f'CREATE TABLE IF NOT EXISTS {table_name} (data_ingestao Date, dado_linha String, tag String) ENGINE = Memory')
    
    insert_dataframe(client, table_name, df)

    client.command(f'DROP TABLE {table_name}')

    assert True