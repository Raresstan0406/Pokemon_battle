class Pokemon:

    def __init__(self, nume, tip, viata, putere_atac):
        self.nume = nume
        self.tip = tip
        self.viata = viata
        self.putere_atac = putere_atac

    def ataca(self, pokemon):
        buffed = ["Apa-Foc", "Foc-Pamant", "Pamant-Apa"]
        viata_initiala = pokemon.viata
        for it in buffed:
            it_split = it.split("-")
            if it_split[0] == self.tip and it_split[1] == pokemon.tip:
                pokemon.viata -= self.putere_atac * 2
                break
        if pokemon.viata == viata_initiala:
            pokemon.viata -= self.putere_atac

    def este_viu(self):
        if self.viata > 0:
            return True
        else:
            return False
