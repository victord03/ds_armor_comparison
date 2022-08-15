from classes.armor_piece import ArmorPiece
from utils.constants import NLNLT, NL


class ArmorSet:
    name: str
    helmet: ArmorPiece
    body: ArmorPiece
    gauntlet: ArmorPiece
    leggings: ArmorPiece

    def __init__(self, data_dict: dict) -> None:
        self.name = data_dict["pn"]
        self.helmet = ArmorPiece(data_dict["helmet"])
        self.body = ArmorPiece(data_dict["body"])
        self.gauntlet = ArmorPiece(data_dict["gauntlet"])
        self.leggings = ArmorPiece(data_dict["leggings"])

    def __repr__(self) -> str:

        intro = f"{NL}{self.name} Armor Set"
        helmet = f"{NLNLT}HELMET {self.helmet.__repr__()}"
        body = f"{NLNLT}BODY {self.body.__repr__()}"
        gauntlet = f"{NLNLT}GAUNTLET {self.gauntlet.__repr__()}"
        leggings = f"{NLNLT}LEGGINGS {self.leggings.__repr__()}"

        return f"{intro}{helmet}{body}{gauntlet}{leggings}"

    @staticmethod
    def compare_armor_piece(self_piece, armor_piece) -> dict:

        # todo: self_piece.copy() -> self_piece_copy.pop("price"), self_piece_copy.pop("armor_piece")
        evaluation = {
            "physical": 0,
            "magical": 0,
            "fire": 0,
            "lightning": 0,
            "price": 0
        }

        for self_key, other_key, in zip(self_piece, armor_piece):
            evaluation[self_key] = self_piece[self_key] - armor_piece[other_key]

        return evaluation

    # todo: does not account specific resistance (only overall score). does not include item cost.
    def compare_armor_set(self, list_of_armor_sets) -> dict:

        best_armor_set = None

        total_scores = dict()

        for armor_set in list_of_armor_sets:

            for armor_set_inner in list_of_armor_sets:
                self_helmet = self.helmet.__dict__
                other_helmet = armor_set.helmet.__dict__

                eval_helmet = self.compare_armor_piece(self_helmet, other_helmet)

                self_body = self.body.__dict__
                other_body = armor_set.body.__dict__

                eval_body = self.compare_armor_piece(self_body, other_body)

                self_gauntlet = self.gauntlet.__dict__
                other_gauntlet = armor_set.gauntlet.__dict__

                eval_gauntlet = self.compare_armor_piece(self_gauntlet, other_gauntlet)

                self_leggings = self.leggings.__dict__
                other_leggings = armor_set.leggings.__dict__

                eval_leggings = self.compare_armor_piece(self_leggings, other_leggings)

                total_scores = {
                    "helmet": sum(list(eval_helmet.values())),
                    "body": sum(list(eval_body.values())),
                    "gauntlet": sum(list(eval_gauntlet.values())),
                    "leggings": sum(list(eval_leggings.values())),
                }

        return total_scores

