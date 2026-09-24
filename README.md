# Pokemon_data_pipeline
A Python CLI application that fetches Pokémon data from the [PokéAPI](https://pokeapi.co/), transforms key attributes (stats, abilities, types, height, weight), and appends the structured results into a JSON file (`pokemon_data.json`).

## Features
- **Interactive CLI**: Search for any Pokémon by name.
- **REST API Integration**: Uses PokéAPI to retrieve up-to-date data.
- **Data Transformation**: Extracts and formats essential details into clean JSON structures.
- **Persistent Storage**: Appends newly fetched Pokémon records to `pokemon_data.json`.

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/pokemon-data-pipeline.git
   cd pokemon-data-pipeline
   ```

2. **Create and activate a virtual environment**:
   - **Windows**:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the pipeline script:

```bash
python Pipeline.py
```

Follow the prompt to enter a Pokémon name (e.g., `pikachu`, `charizard`) or type `quit` to exit.


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
