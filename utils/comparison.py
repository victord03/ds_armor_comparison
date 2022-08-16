
def compare_armor_sets(armor_set_a, armor_set_b) -> dict:

    evaluation = {

        "helmet": {
            "physical": 0,
            "magical": 0,
            "fire": 0,
            "lightning": 0,
            "price": 0,
            "weight": 0,
        },
        "body": {
            "physical": 0,
            "magical": 0,
            "fire": 0,
            "lightning": 0,
            "price": 0,
            "weight": 0,
        },
        "gauntlet": {
            "physical": 0,
            "magical": 0,
            "fire": 0,
            "lightning": 0,
            "price": 0,
            "weight": 0,
        },
        "leggings": {
            "physical": 0,
            "magical": 0,
            "fire": 0,
            "lightning": 0,
            "price": 0,
            "weight": 0,
        },
    }

    armor_set_a_as_dict = armor_set_a.__dict__
    armor_set_b_as_dict = armor_set_b.__dict__

    for armor_set_a_key, armor_set_b_key in zip(armor_set_a_as_dict, armor_set_b_as_dict):

        if armor_set_a_key == "name" or armor_set_a_key == "weight":
            continue
        else:

            self_armor_piece_dict = armor_set_a_as_dict[armor_set_a_key].resistances.__dict__
            other_armor_piece_dict = armor_set_b_as_dict[armor_set_b_key].resistances.__dict__

            for self_res_name in self_armor_piece_dict:
                self_res_value = self_armor_piece_dict[self_res_name]
                other_res_value = other_armor_piece_dict[self_res_name]

                evaluation[armor_set_a_key][self_res_name] = self_res_value - other_res_value

    for armor_set_a_key, armor_set_b_key in zip(armor_set_a_as_dict, armor_set_b_as_dict):

        if armor_set_a_key == "name" or armor_set_a_key == "weight":
            continue
        else:

            armor_a_price = armor_set_a_as_dict[armor_set_a_key].attributes.price
            armor_b_price = armor_set_b_as_dict[armor_set_b_key].attributes.price

            evaluation[armor_set_a_key]['price'] = armor_a_price - armor_b_price

            armor_set_a_weight = armor_set_a_as_dict[armor_set_a_key].attributes.weight
            armor_set_b_weight = armor_set_b_as_dict[armor_set_b_key].attributes.weight
            evaluation[armor_set_a_key]['weight'] = round(armor_set_a_weight - armor_set_b_weight, 1)

    return evaluation


def maximize_this_resistance(armor_set_a, armor_set_b, resistance: str) -> dict:

    armor_set_a_as_a_dict = armor_set_a.__dict__
    armor_set_b_as_a_dict = armor_set_b.__dict__

    armor_set_a_copy = armor_set_a_as_a_dict.copy()
    armor_set_a_copy.pop("name")

    armor_set_b_copy = armor_set_b_as_a_dict.copy()
    armor_set_b_copy.pop("name")

    evaluation = {
        "helmet": (str, int),
        "body":  (str, int),
        "gauntlet":  (str, int),
        "leggings":  (str, int),
    }

    for key in armor_set_a_copy:
        # todo: fix this
        resistances_a_as_dict = armor_set_a_copy[key].resistances.__dict__
        resistances_b_as_dict = armor_set_b_copy[key].resistances.__dict__

        for value_armor_set_a, value_armor_set_b in zip(resistances_a_as_dict, resistances_b_as_dict):

            if value_armor_set_a == resistance:

                a_is_higher = resistances_a_as_dict[value_armor_set_a] > resistances_b_as_dict[value_armor_set_b]

                if a_is_higher:
                    diff = resistances_a_as_dict[value_armor_set_a] - resistances_b_as_dict[value_armor_set_b]
                    evaluation[key] = (armor_set_a_as_a_dict["name"], diff)
                else:
                    diff = resistances_b_as_dict[value_armor_set_b] - resistances_a_as_dict[value_armor_set_a]
                    evaluation[key] = (armor_set_b_as_a_dict["name"], diff)

    return evaluation


# WIP
def compare_multiple_armor_sets(self, list_of_armor_sets) -> dict:

    best_armor_set = None

    total_scores = dict()

    for armor_set in list_of_armor_sets:

        self_helmet = self.helmet.__dict__
        other_helmet = armor_set.helmet.__dict__

        eval_helmet = compare_armor_sets(self_helmet, other_helmet)

        self_body = self.body.__dict__
        other_body = armor_set.body.__dict__

        eval_body = compare_armor_sets(self_body, other_body)

        self_gauntlet = self.gauntlet.__dict__
        other_gauntlet = armor_set.gauntlet.__dict__

        eval_gauntlet = compare_armor_sets(self_gauntlet, other_gauntlet)

        self_leggings = self.leggings.__dict__
        other_leggings = armor_set.leggings.__dict__

        eval_leggings = compare_armor_sets(self_leggings, other_leggings)

        total_scores = {
            "helmet": sum(list(eval_helmet.values())),
            "body": sum(list(eval_body.values())),
            "gauntlet": sum(list(eval_gauntlet.values())),
            "leggings": sum(list(eval_leggings.values())),
        }

    return total_scores
