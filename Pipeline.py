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

def save_pokemon_data_to_json(pokemon_data, file_name):
    try:
        with open(file_name, "r") as json_file:
            data_list = json.load(json_file)
    except FileNotFoundError:
        data_list = []

    data_list.append(pokemon_data)

    with open(file_name, "w") as json_file:
        json.dump(data_list, json_file, indent=4)

def pipeline():
    pokemon_name = input("Enter the name of the Pokemon (or type 'quit' to exit): ").strip().lower()

    if pokemon_name == 'quit':
        return False 
        
    pokemon_data = fetch_pokemon_data(pokemon_name)

    if pokemon_data:
        transformed_data = transform_pokemon_data(pokemon_data)
        save_pokemon_data_to_json(transformed_data, "pokemon_data.json")
        print(f"Data for '{pokemon_name}' has been saved to pokemon_data.json.\n")
    else:
        print("Failed to fetch data. Please check the spelling.\n")
        
    return True

if __name__ == "__main__":
    print("Welcome to the Pokedex fetcher!")
    while pipeline():
        pass
    