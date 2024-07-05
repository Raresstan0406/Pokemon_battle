from Pokemon import Pokemon
from Antrenor import Antrenor
from Batalie import Batalie
import random
pokemoni_list = []
with open('pokemoni.txt', 'r') as file:
    pokemoni_list=file.read().splitlines()
antrenor1 = Antrenor(" ", [])
antrenor2 = Antrenor(" ", [])
nume_1 = input("Nume antrenor 1: ")
antrenor1.nume = nume_1
nr_1 = input("Introduceti numarul de pokemoni:")
introdus_random_1 = input("Introduce / Alege random din lista standard :")
if introdus_random_1 == "Introduce":
    for i in range(1, int(nr_1) + 1):
        pokemon = input(f"Pokemon {i}: ")
        pokemon_split = pokemon.split(" ")
        antrenor1.pokemoni.append(Pokemon(pokemon_split[0], pokemon_split[1], int(pokemon_split[2]), int(pokemon_split[3])))
elif introdus_random_1 == "Alege":
    for i in range(1, int(nr_1) + 1):
        pokemon = random.choice(pokemoni_list)
        pokemon_split = pokemon.split(" ")
        antrenor1.pokemoni.append(Pokemon(pokemon_split[0], pokemon_split[1], int(pokemon_split[2]), int(pokemon_split[3])))
        print(f"Pokemon {i} : {pokemon}")
nume_2 = input("Nume antrenor 2: ")
antrenor2.nume = nume_2
nr_2 = input("Introduceti numarul de pokemoni:")
introdus_random_2 = input("Introduce / Alege random din lista standard : ")

if introdus_random_2 == "Introduce":
    for i in range(1, int(nr_2) + 1):
        pokemon = input(f"Pokemon {i}: ")
        pokemon_split = pokemon.split(" ")
        antrenor2.pokemoni.append(Pokemon(pokemon_split[0], pokemon_split[1], int(pokemon_split[2]), int(pokemon_split[3])))
elif introdus_random_2 == "Alege":
    for i in range(1, int(nr_2) + 1):
        pokemon = random.choice(pokemoni_list)
        pokemon_split = pokemon.split(" ")
        antrenor2.pokemoni.append(Pokemon(pokemon_split[0], pokemon_split[1], int(pokemon_split[2]), int(pokemon_split[3])))
        print(f"Pokemon {i} : {pokemon}")

batalie = Batalie()
batalie.lupta(antrenor1, antrenor2)
