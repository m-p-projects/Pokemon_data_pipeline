# Pokemon_data_pipeline
Python ETL pipeline that fetches, transforms, and stores data from the public PokéAPI.

## Project Description
This project is a Python-based ETL data pipeline. It fetches data from the public [PokéAPI](https://pokeapi.co/), extracts and transforms key attributes for selected Pokémon (such as types, abilities, and base stats), and stores the structured dataset in a clean JSON file.

## How to run script (Git + Python already installed)
1. Navigate to save location (Desktop)
```cd %USERPROFILE%\Desktop```
2. Clone the repository
Open your terminal or command prompt and clone the repository to your local machine:
```
git clone https://github.com/m-p-projects/Pokemon_data_pipeline.git
```
3. Navigate to the project directory
```cd Pokemon_data_pipeline```
4. Run the script
```python Pipeline.py```


## Example Output
[
    {
        "id": 1,
        "name": "Bulbasaur",
        "height": 7,
        "weight": 69,
        "abilities": [
            "overgrow",
            "chlorophyll"
        ],
        "types": [
            "grass",
            "poison"
        ],
        "stats": {
            "hp": 45,
            "attack": 49,
            "defense": 49,
            "special-attack": 65,
            "special-defense": 65,
            "speed": 45
        }
    }
]

## Explaination
The pipeline script is designed around three standard ETL phases:

Extract: Uses the requests library to make HTTP GET requests to the PokéAPI for a predefined list of Pokémon. It includes error handling for failed network requests.

Transform: Parses the massive, deeply nested JSON response returned by the API. It strips away unnecessary data, flattens nested lists, and maps the relevant fields (Name, Types, Abilities, Stats, Height, Weight) into a simplified, easy-to-read dictionary structure.

Load: Collects the transformed dictionaries and exports them into a neatly formatted .json file for future analysis or storage.
