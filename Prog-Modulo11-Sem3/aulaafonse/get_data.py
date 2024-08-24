import requests

def get_all_pokemon(url='https://pokeapi.co/api/v2/pokemon?limit=1118'):
    """
    Fetches data about all pokemon from the PokeAPI.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data: {}".format(response.status_code))
    return response.json()