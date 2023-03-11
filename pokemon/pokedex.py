import json
from Pokemon import Pokemon

class Pokedex:
    def __init__(self):
        self.pokemons = []

    def load_pokemons(self, file_name):
        try:
            with open(file_name, 'r') as f:
                data = json.load(f)
                for p in data:
                    pokemon = Pokemon(p['name'], p['type'], p['defense'], p['attack'], p['life'])
                    if not self.is_duplicate(pokemon):
                        self.pokemons.append(pokemon)
        except FileNotFoundError:
            print(f"{file_name} not found")

    def save_pokemon(self, pokemon, file_name):
        if not self.is_duplicate(pokemon):
            self.pokemons.append(pokemon)
            with open(file_name, 'w') as f:
                data = []
                for p in self.pokemons:
                    data.append({'name': p.name, 'type': p.type, 'defense': p.defense, 'attack': p.attack, 'life': p.life})
                json.dump(data, f)

    def is_duplicate(self, pokemon):
        for p in self.pokemons:
            if p.name == pokemon.name:
                return True
        return False

    def print_pokemons(self):
        print(f"Number of Pokemons: {len(self.pokemons)}")
        for p in self.pokemons:
            p.print_info()
