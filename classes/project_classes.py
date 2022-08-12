
class ArmorPiece:
    armor_piece: int
    physical: int
    magical: int
    fire: int
    lighting: int
    price: int

    def __init__(self, data_dict: dict) -> None:
        self.armor_piece = data_dict["armor_piece"]
        self.physical = data_dict["physical"]
        self.magical = data_dict["magical"]
        self.fire = data_dict["fire"]
        self.lighting = data_dict["lightning"]
        self.price = data_dict["price"]

    def __repr__(self) -> str:
        return f"\n\t\tPHYS {self.physical}\n\t\tMAG {self.magical}\n\t\tFIRE {self.fire}\n\t\tLIGHT" \
               + f" {self.lighting}\n\t\tPRICE {self.price:,}"


class ArmorSet:
    name: str
    helmet: ArmorPiece
    body: ArmorPiece
    gauntlet: ArmorPiece
    leggings: ArmorPiece

    def __init__(self, data_dict: dict) -> None:
        self.name = data_dict["name"]
        self.helmet = ArmorPiece(data_dict["helmet"])
        self.body = ArmorPiece(data_dict["body"])
        self.gauntlet = ArmorPiece(data_dict["gauntlet"])
        self.leggings = ArmorPiece(data_dict["leggings"])

    def __repr__(self) -> str:
        return f"\n{self.name} Armor Set\n\n\tHELMET{self.helmet.__repr__()}" \
               + f"\n\n\tBODY{self.body.__repr__()}\n\n\tGAUNTLET{self.gauntlet.__repr__()}" \
               + f"\n\n\tLEGGINGS{self.leggings.__repr__()}"

    def compare_armor_sets(self, armor_set) -> None:

        attributes = list(self.helmet.__dict__.keys())
        attributes_2 = [attribute for attribute in self.helmet.__dict__]
        print(attributes)
        print(attributes_2)

