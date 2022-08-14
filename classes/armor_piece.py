class APAttributes:
    armor_piece: str
    price: int

    def __init__(self, armor_piece: str, price: int) -> None:
        self.armor_piece = armor_piece
        self.price = price


class APResistances:
    physical: int
    magical: int
    fire: int
    lighting: int

    def __init__(self, physical: int, magical: int, fire: int, lighting: int) -> None:
        self.physical = physical
        self.magical = magical
        self.fire = fire
        self.lighting = lighting


class ArmorPiece:
    resistances: APResistances
    attributes: APAttributes

    def __init__(self, data_dict: dict) -> None:
        self.resistances = APResistances(data_dict["physical"], data_dict["magical"], data_dict["fire"], data_dict["lightning"])
        self.attributes = APAttributes(data_dict["price"], data_dict["armor_piece"])

    def __repr__(self) -> str:
        return f"{self.resistances.__dict__}"
