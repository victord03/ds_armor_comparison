from classes.armor_piece import ArmorPiece
from utils.constants import NLNLT, NL


class ArmorSet:
    name: str
    helmet: ArmorPiece
    body: ArmorPiece
    gauntlet: ArmorPiece
    leggings: ArmorPiece
    weight: float

    def __init__(self, data_dict: dict) -> None:
        self.name = data_dict["pn"]
        self.helmet = ArmorPiece(data_dict["helmet"])
        self.body = ArmorPiece(data_dict["body"])
        self.gauntlet = ArmorPiece(data_dict["gauntlet"])
        self.leggings = ArmorPiece(data_dict["leggings"])

        self.weight = self.helmet.attributes.weight + self.body.attributes.weight
        self.weight += self.gauntlet.attributes.weight + self.leggings.attributes.weight

    def show_self(self) -> str:

        intro = f"{NL}{self.name} Armor Set"
        helmet = f"{NLNLT}HELMET {self.helmet.__repr__()}"
        body = f"{NLNLT}BODY {self.body.__repr__()}"
        gauntlet = f"{NLNLT}GAUNTLET {self.gauntlet.__repr__()}"
        leggings = f"{NLNLT}LEGGINGS {self.leggings.__repr__()}"

        return f"{intro}{helmet}{body}{gauntlet}{leggings}"

    def self_as_dict(self) -> dict:
        return self.__dict__
