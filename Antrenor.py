class Antrenor:

    def __init__(self, nume, pokemoni):
        self.nume = nume
        self.pokemoni = pokemoni

    def alege_pokemon(self):
        for pokemon in self.pokemoni:
            if pokemon.este_viu():
                return pokemon

    def are_pokemoni_vii(self):
        for pokemon in self.pokemoni:
            if pokemon.este_viu():
                return True
        return False
