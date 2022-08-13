
class ArmorPiece:
    armor_piece: int
    physical: int
    magical: int
    fire: int
    lighting: int
    price: int

    def __init__(self, data_dict: dict) -> None:
        # self.armor_piece = data_dict["armor_piece"]
        self.physical = data_dict["physical"]
        self.magical = data_dict["magical"]
        self.fire = data_dict["fire"]
        self.lighting = data_dict["lightning"]
        # self.price = data_dict["price"]

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

    @staticmethod
    def compare_armor_piece(self_piece, armor_piece) -> dict:

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
    def compare_armor_set(self, armor_set):

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
            "helmet": sum([x for x in eval_helmet.values()]),
            "body": sum([x for x in eval_body.values()]),
            "gauntlet": sum([x for x in eval_gauntlet.values()]),
            "leggings": sum([x for x in eval_leggings.values()]),
        }

        return total_scores

