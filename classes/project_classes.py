
class ArmorPiece:
    # name: str
    # armor_piece: str
    physical: int
    magical: int
    fire: int
    lighting: int
    price: int

    def __init__(
            self, name: str, armor_piece: int, physical: int, magical: int, fire: int, lighting: int, price: int
    ) -> None:
        self.name = name
        self.armor_piece = armor_piece
        self.physical = physical
        self.magical = magical
        self.fire = fire
        self.lighting = lighting
        self.price = price

    def __repr__(self) -> str:
        return f"\n\t\tPHYS {self.physical}\n\t\tMAG {self.magical}\n\t\tFIRE {self.fire}\n\t\tLIGHT" \
               + f"{self.lighting}\n\t\tPRICE {self.price:,}"


class ArmorSet:
    name: str
    helmet: ArmorPiece
    body: ArmorPiece
    gauntlet: ArmorPiece
    leggings: ArmorPiece

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"\n{self.name} Armor Set\n\n\tHELMET{self.helmet.__repr__()}" \
               + f"\n\n\tBODY{self.body.__repr__()}\n\n\tGAUNTLET{self.gauntlet.__repr__()}" \
               + f"\n\n\tLEGGINGS{self.leggings.__repr__()}"

    def complete_set(self, helmet: ArmorPiece, body: ArmorPiece, gauntlet: ArmorPiece, leggings: ArmorPiece) -> None:
        self.helmet = helmet
        self.body = body
        self.gauntlet = gauntlet
        self.leggings = leggings

    def compare_armor_sets(self, other: any):

        attributes = list(self.helmet.__dict__.keys())
        attributes_2 = [attribute for attribute in self.helmet.__dict__]
        print(attributes)
        print(attributes_2)

        # for each in attributes:
            # print(self.helmet.each)
