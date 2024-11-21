import requests
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text



"""
pikachu,
[{'ability': {'name': 'static', 'url': 'https://pokeapi.co/api/v2/ability/9/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'lightning-rod', 'url': 'https://pokeapi.co/api/v2/ability/31/'}, 'is_hidden': True, 'slot': 3}]
"""

pikachu_data = json.loads(json_data)

print(".      .")
print(pikachu_data["name"])
print(pikachu_data["abilities"])
print("-----------------------------------------------------------------------------------------------------------""\n")

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {pokemon_name}. Status code: {response.status_code}")
        return None

def display_pokemon_info(pokemon_list):
    total_weight = 0
    count = 0
    for pokemon_name in pokemon_list:
        data = fetch_pokemon_data(pokemon_name)
        if data:
            print(f"{pokemon_name.title()}")
            print(f"Weight: {data['weight']}")

            print("Abilities (Formatted):")
            for ability_data in data['abilities']:
                print(f"  - {ability_data['ability']['name']} ({'Hidden' if ability_data['is_hidden'] else 'Normal'})")

            print("Abilities (Raw JSON):")
            raw_data = {"weight": data["weight"], "abilities": data["abilities"]} 
            print(json.dumps(raw_data, indent=4))

            total_weight += data['weight']
            count += 1
        else:
            print(f"Warning: Could not get weight for {pokemon_name}")

    if count > 0:
        average_weight = total_weight / count
        print(f"\nAverage weight: {average_weight}")
    else:
        print("No valid weight data found.")

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
display_pokemon_info(pokemon_names)