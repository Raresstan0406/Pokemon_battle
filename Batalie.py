from Pokemon import Pokemon
class Batalie:

    def lupta(self, antrenor1, antrenor2):
        pokemon_antrenor_1 = Pokemon("", "", 0, 0)
        pokemon_antrenor_2 = Pokemon("", "", 0, 0)
        print("1. Alegeti un pokemon:")
        for pokemon in antrenor1.pokemoni:
            print(pokemon.nume)
        choice_antrenor_1 = input(f"1. Alegerea ta:")
        print("2. Alegeti un pokemon:")
        for pokemon in antrenor2.pokemoni:
            print(pokemon.nume)
        choice_antrenor_2 = input(f"2. Alegerea ta:")
        for pokemon in antrenor1.pokemoni:
            if pokemon.nume == choice_antrenor_1:
                pokemon_antrenor_1 = pokemon
        for pokemon in antrenor2.pokemoni:
            if pokemon.nume == choice_antrenor_2:
                pokemon_antrenor_2 = pokemon
        while antrenor1.are_pokemoni_vii() and antrenor2.are_pokemoni_vii():
            while pokemon_antrenor_1.este_viu() and pokemon_antrenor_2.este_viu():
                if pokemon_antrenor_2.este_viu():
                    pokemon_antrenor_1.ataca(pokemon_antrenor_2)
                if pokemon_antrenor_1.este_viu():
                    pokemon_antrenor_2.ataca(pokemon_antrenor_1)
            if not pokemon_antrenor_1.este_viu():
                pokemon_antrenor_1 = antrenor1.alege_pokemon()
            if not pokemon_antrenor_2.este_viu():
                pokemon_antrenor_2 = antrenor2.alege_pokemon()
            if not antrenor1.are_pokemoni_vii() or not antrenor2.are_pokemoni_vii():
                print(f" Antrenor 1 : {antrenor1.nume}")
                for pokemon in antrenor1.pokemoni:
                    if not pokemon.este_viu():
                        print(f"{pokemon.nume} : Mort")
                    else:
                        print(f"{pokemon.nume} : {pokemon.viata}")
                print(f" Antrenor 2 : {antrenor2.nume}")
                for pokemon in antrenor2.pokemoni:
                    if not pokemon.este_viu():
                        print(f"{pokemon.nume} : Mort")
                    else:
                        print(f"{pokemon.nume} : {pokemon.viata}")
                if antrenor1.are_pokemoni_vii():
                    print("Antrenorul 1 a castigat")
                if antrenor2.are_pokemoni_vii():
                    print("Antrenorul 2 a castigat")





