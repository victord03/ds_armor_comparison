from utils.constants import NL, T


class APAttributes:
    """Armor piece Attributes.

    The attributes are only weight and price which
    are compared differently than resistances (APResistances class)."""

    weight: float
    price: int

    def __init__(self, price: int, weight: float) -> None:
        """Init method.

        Takes the only two attributes the class tracks as arguments and stores them."""

        self.price = price
        self.weight = weight


class APResistances:
    """Armor piece Resistances.

    Stores the resistances linked to each ArmorPiece."""

    physical: int
    magical: int
    fire: int
    lightning: int

    def __init__(self, physical: int, magical: int, fire: int, lightning: int) -> None:
        """Init method.

        Takes the attributes the class tracks as arguments and stores them."""

        self.physical = physical
        self.magical = magical
        self.fire = fire
        self.lightning = lightning


class ArmorPiece:
    """Armor piece class.

    Comprised of
    1) resistances (APResistances) and
    2) attributes (APAttributes)

    which are dictionaries and allow for easy iteration using keys."""

    resistances: APResistances
    attributes: APAttributes

    def __init__(self, data_dict: dict) -> None:
        """Init method.

        Gets a 'data_dict' as an argument and expects it to have all the exact keys corresponding to the
        attributes of the two composed classes, APResistances and APAttributes.

        Separates them and instantiates a class for each of the two."""

        self.resistances = APResistances(
            data_dict["physical"], data_dict["magical"], data_dict["fire"], data_dict["lightning"]
        )

        self.attributes = APAttributes(data_dict["price"], data_dict["weight"])

    # todo: move to UI
    def show_self(self) -> str:
        """Displays all information about the ArmorPiece."""

        physical = f"{NL}{T}{T}Physical: {self.resistances.physical}"
        magical = f"{NL}{T}{T}Magical: {self.resistances.magical}"
        fire = f"{NL}{T}{T}Fire: {self.resistances.fire}"
        lightning = f"{NL}{T}{T}Lightning: {self.resistances.lightning}"

        price = f"{NL}{T}{T}Price: {self.attributes.price}"
        weight = f"{NL}{T}{T}Price: {self.attributes.weight}"

        return f"{physical}{magical}{fire}{lightning}{price}{weight}"

    def self_as_dict(self) -> dict:
        """Returns the instance as a dict for iterative usage."""
        return self.__dict__
