import project_classes


def give_part_index_and_name(part: str) -> tuple[int, str]:

    match part.lower():
        case "h":
            return 1, "Helmet"
        case "b":
            return 2, "Body"
        case "g":
            return 3, "Gauntlet"
        case "l":
            return 4, "Leggings"


def create_armor_pieces(set_stats: dict) -> tuple[project_classes.ArmorPiece, ...]:

    index, word = give_part_index_and_name("h")
    sh = project_classes.ArmorPiece(
        # set_stats["Name"],
        # list(set_stats.keys())[index],
        *set_stats[word]
    )

    index, word = give_part_index_and_name("b")
    sb = project_classes.ArmorPiece(
        # set_stats["Name"],
        # list(set_stats.keys())[index],
        *set_stats[word]
    )

    index, word = give_part_index_and_name("g")
    sg = project_classes.ArmorPiece(
        # set_stats["Name"],
        # list(set_stats.keys())[index],
        *set_stats[word]
    )

    index, word = give_part_index_and_name("l")
    sl = project_classes.ArmorPiece(
        # set_stats["Name"],
        # list(set_stats.keys())[index],
        *set_stats[word]
    )

    return sh, sb, sg, sl


def create_armor_set(set_name: str, set_pieces: tuple[project_classes.ArmorPiece, ...]) -> project_classes.ArmorSet:

    my_set: project_classes.ArmorSet = project_classes.ArmorSet(set_name)
    my_set.complete_set(*set_pieces)

    return my_set


def main():

    steel_set_stats = {
        # "Name": "Steel",
        "Helmet": (16, 8, 8, 5, 5_000),
        "Body": (42, 22, 21, 13, 8_000),
        "Gauntlet": (25, 13, 12, 8, 5_000),
        "Leggings": (25, 13, 12, 8, 5_000)
    }

    balder_set_stats = {
        "Name": "Balder",
        "Helmet": (14, 6, 8, 6, 5_000),
        "Body": (37, 15, 18, 15, 8_000),
        "Gauntlet": (17, 7, 8, 5, 5_000),
        "Leggings": (22, 10, 12, 9, 5_000),
    }

    steel_set = create_armor_set("Steel", create_armor_pieces(steel_set_stats))
    balder_set = create_armor_set("Balder", create_armor_pieces(balder_set_stats))

    # print(steel_set)
    # print(balder_set)

    steel_set.compare_armor_sets(balder_set)


if __name__ == "__main__":
    main()
