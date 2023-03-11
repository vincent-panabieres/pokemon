import random
import json
from Pokemon import Pokemon
from type import Type
from combat import Combat
from pokedex import Pokedex

with open('pokedex.json', 'r') as f:
    pokedex = json.load(f)

types = [
    Type('Normal', 100, 10, 0),
    Type('Feu', 100, 20, 5),
    Type('Eau', 120, 15, 10),
    Type('Terre', 150, 5, 20)
]

pokemon_names = ['Pikachu', 'Bulbasaur', 'Charmander', 'Squirtle']

print("Choisissez votre Pokémon:")
for i, name in enumerate(pokemon_names):
    print(f"{i+1}. {name}")
player_pokemon = None
while player_pokemon is None:
    try:
        choice = int(input("Votre choix: "))
        if choice < 1 or choice > len(pokemon_names):
            raise ValueError
        player_pokemon = Pokemon(pokemon_names[choice-1], types[random.randint(0,3)])
    except ValueError:
        print("Choix invalide.")

opponent_pokemon = None
while opponent_pokemon is None:
    try:
        name, data = random.choice(list(pokedex.items()))
        opponent_pokemon = Pokemon(name, types[data['type']])
    except:
        pass

combat = Combat(player_pokemon, opponent_pokemon)

print("Début du combat!")
print(f"Vous avez choisi {player_pokemon.name}")
print(f"Votre adversaire est {opponent_pokemon.name}")
while not combat.is_finished():
    print(f"Tour {combat.round}:")
    combat.play_round()
    print(f"{player_pokemon.name} - PV: {player_pokemon.hp} / {player_pokemon.type.hp}, Défense: {player_pokemon.defense}, Attaque: {player_pokemon.type.attack}")
    print(f"{opponent_pokemon.name} - PV: {opponent_pokemon.hp} / {opponent_pokemon.type.hp}, Défense: {opponent_pokemon.defense}, Attaque: {opponent_pokemon.type.attack}")

winner = combat.get_winner()
if winner == player_pokemon:
    print("Vous avez gagné!")
else:
    print(f"{opponent_pokemon.name} a gagné.")    

pokedex[player_pokemon.name] = {
    'type': player_pokemon.type.name,
    'hp': player_pokemon.type.hp,
    'attack': player_pokemon.type.attack,
    'defense': player_pokemon.defense
}
with open('pokedex.json', 'w') as f:
    json.dump(pokedex, f)

print("Pokédex:")
for name, data in pokedex.items():
    print(f"- {name} ({data['type']})")
