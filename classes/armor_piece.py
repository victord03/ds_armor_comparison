from utils.constants import NL, T


class APAttributes:
    price: int

    def __init__(self, price: int) -> None:
        self.price = price


class APResistances:
    physical: int
    magical: int
    fire: int
    lightning: int

    def __init__(self, physical: int, magical: int, fire: int, lightning: int) -> None:
        self.physical = physical
        self.magical = magical
        self.fire = fire
        self.lightning = lightning


class ArmorPiece:
    resistances: APResistances
    attributes: APAttributes

    def __init__(self, data_dict: dict) -> None:

        self.resistances = APResistances(
            data_dict["physical"], data_dict["magical"], data_dict["fire"], data_dict["lightning"]
        )

        self.attributes = APAttributes(data_dict["price"])

    def __repr__(self) -> str:

        physical = f"{NL}{T}{T}Physical: {self.resistances.physical}"
        magical = f"{NL}{T}{T}Magical: {self.resistances.magical}"
        fire = f"{NL}{T}{T}Fire: {self.resistances.fire}"
        lightning = f"{NL}{T}{T}Lightning: {self.resistances.lightning}"

        price = f"{NL}{T}{T}Price: {self.attributes.price}"

        return f"{physical}{magical}{fire}{lightning}{price}"
