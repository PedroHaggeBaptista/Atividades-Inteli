# Faça o teste para process_data e prepare_dataframe_for_insert em tests/data_processing_test.py.

import pytest
import pandas as pd
from datetime import date
from aulaafonse.data_processing import process_data, prepare_dataframe_for_insert

def test_process_data():
    data = {
        'name': 'Pikachu',
        'type': 'Electric'
    }
    filename = process_data(data)
    assert filename is not None

def test_prepare_dataframe_for_insert():
    actualDate = date.today()
    df = pd.DataFrame({
        'name': ['Pikachu', 'Charmander', 'Squirtle'],
        'type': ['Electric', 'Fire', 'Water']
    })
    df['data_ingestao'] = actualDate
    df['dado_linha'] = df.apply(lambda row: row.to_json(), axis=1)
    df['tag'] = 'pokemon'
    df = df[['data_ingestao', 'dado_linha', 'tag']]
    prepared_df = prepare_dataframe_for_insert(df)
    assert prepared_df is not None
    assert len(prepared_df) == 3
    assert 'data_ingestao' in prepared_df.columns
    assert 'dado_linha' in prepared_df.columns
    assert 'tag' in prepared_df.columns
    assert prepared_df['tag'].unique()[0] == 'pokemon'
    assert prepared_df['data_ingestao'].unique()[0].date() == actualDate