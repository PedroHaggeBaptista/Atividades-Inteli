from aulaafonse.get_data import get_all_pokemon

def test_get_all_pokemon():
    data = get_all_pokemon()
    assert data is not None
    assert 'results' in data
    assert len(data['results']) == 1118
    assert 'name' in data['results'][0]
    assert 'url' in data['results'][0]