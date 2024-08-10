import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
            "base_stats" : [stats["base_stat"] for stats in pokemon_data["stats"]],
            "effort" : [(ev["effort"], ev["stat"]["name"]) for ev in pokemon_data["stats"] if ev["effort"] > 0]
        }
        return pokemon_info
    else:
        return None
    
pokemon_name = input("Enter the Pokémon name: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Abilities: {', '.join(pokemon_info['abilities'])}")
    print(f"Types: {', '.join(pokemon_info['types'])}")
    #region Stats
    print(f"HP: {pokemon_info["base_stats"][0]}")
    print(f"ATK: {pokemon_info["base_stats"][1]}")
    print(f"DEF: {pokemon_info["base_stats"][2]}")
    print(f"SPATK: {pokemon_info["base_stats"][3]}")
    print(f"SPDEF: {pokemon_info["base_stats"][4]}")
    print(f"SPD: {pokemon_info["base_stats"][5]}")
    print(f"Total: {sum(pokemon_info["base_stats"])}")
    #endregion
    ev_yield = ', '.join(f"{effort} {stat}" for effort, stat in pokemon_info['effort'])
    print(f"EV Yield: {ev_yield}")

else:
    print("Pokémon not found!")