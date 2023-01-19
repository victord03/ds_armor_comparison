
def compare_armor_sets(armor_set_a, armor_set_b) -> dict:
    """Takes two armor sets and compares them.

    Iteratively scans and stores each value difference to an 'evaluation' dict.

    Positive values mean that 'armor_set_a' has that much higher value in the specified
    category and negative values mean that 'armor_set_b' has that much of a higher value
    in the specified category.

    Returns the entire dict to allow multiple usages and to lean toward a single-purpose
    function."""

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
    """Has critical flaws at the moment.

    Compares two armor sets and will return a configuration where for each slot, the armor
    with the highest resistance selected is chosen. Effectively 'maximizing for this resistance'."""

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

    # todo: Needs fixing. Think about creating a separate function for the looping. Think about reading then storing
    # todo: all values, then compiling a dictionary from scratch, instead of reading and compiling the dict in real time
    for key in armor_set_a_copy:
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
    """Compares an arbitrary number of armor sets, given as a list of instances,
    scores them, and returns a list of evaluation scores."""

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
