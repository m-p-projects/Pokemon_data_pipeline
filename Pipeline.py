import requests
import json

API_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_pokemon_data(pokemon_name):
    url = f"{API_URL}/{pokemon_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def transform_pokemon_data(pokemon_data):
    transformed_data = {
        "id": pokemon_data.get("id"),
        "name": pokemon_data.get("name"),
        "base_experience": pokemon_data.get("base_experience"),
        "height": pokemon_data.get("height"),
        "weight": pokemon_data.get("weight"),
        "abilities": [ability["ability"]["name"] for ability in pokemon_data.get("abilities", [])],
        "stats": [stat["stat"]["name"] for stat in pokemon_data.get("stats", [])],
        "types": [type_["type"]["name"] for type_ in pokemon_data.get("types", [])]
    }
    return transformed_data

def load_pokemon_data_from_json(file_name="pokemon_data.json"):
    try:
        with open(file_name, "r") as json_file:
            data_list = json.load(json_file)
            if isinstance(data_list, list):
                return data_list
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []

def pokemon_exists_in_json(pokemon_identifier, file_name="pokemon_data.json"):
    data_list = load_pokemon_data_from_json(file_name)
    identifier_clean = str(pokemon_identifier).strip().lower()
    for item in data_list:
        if (item.get("name") or "").lower() == identifier_clean:
            return True
        if str(item.get("id")) == identifier_clean:
            return True
    return False

def save_pokemon_data_to_json(pokemon_data, file_name="pokemon_data.json"):
    data_list = load_pokemon_data_from_json(file_name)

    # Prevent duplicates: remove any existing entry matching name or id
    pokemon_name = (pokemon_data.get("name") or "").lower()
    pokemon_id = pokemon_data.get("id")
    data_list = [
        item for item in data_list
        if (item.get("name") or "").lower() != pokemon_name
        and (pokemon_id is None or item.get("id") != pokemon_id)
    ]
    data_list.append(pokemon_data)

    # Sort alphabetically by Pokémon name
    data_list.sort(key=lambda item: (item.get("name") or "").lower())

    with open(file_name, "w") as json_file:
        json.dump(data_list, json_file, indent=4)

def pipeline():
    data_file = "pokemon_data.json"
    try:
        pokemon_name = input("Enter the name of the Pokemon (or type 'quit' to exit): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return False

    if not pokemon_name or pokemon_name == 'quit':
        return False 

    # Check local file before making HTTP request to PokeAPI
    if pokemon_exists_in_json(pokemon_name, data_file):
        print(f"Notice: '{pokemon_name}' already exists in {data_file}. Skipping API call.\n")
        return True

    pokemon_data = fetch_pokemon_data(pokemon_name)

    if pokemon_data:
        transformed_data = transform_pokemon_data(pokemon_data)
        save_pokemon_data_to_json(transformed_data, data_file)
        print(f"Data for '{pokemon_name}' has been saved to {data_file}.\n")
    else:
        print("Failed to fetch data. Please check the spelling.\n")
        
    return True

if __name__ == "__main__":
    print("Welcome to the Pokedex fetcher!")
    try:
        while pipeline():
            pass
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

    