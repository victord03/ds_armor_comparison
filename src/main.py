from classes.project_classes import ArmorPiece, ArmorSet
import data.armor_sets as dt_arm_sts


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


def create_armor_pieces(set_stats: dict) -> tuple[ArmorPiece, ...]:

    index, word = give_part_index_and_name("h")
    sh = ArmorPiece(
        *set_stats[word]
    )

    index, word = give_part_index_and_name("b")
    sb = ArmorPiece(
        *set_stats[word]
    )

    index, word = give_part_index_and_name("g")
    sg = ArmorPiece(
        *set_stats[word]
    )

    index, word = give_part_index_and_name("l")
    sl = ArmorPiece(
        *set_stats[word]
    )

    return sh, sb, sg, sl


def create_armor_set(set_name: str, set_pieces: tuple[ArmorPiece, ...]) -> ArmorSet:

    my_set: ArmorSet = ArmorSet(set_name)
    my_set.complete_set(*set_pieces)

    return my_set


def main():

    steel_set = create_armor_set("Steel", create_armor_pieces(dt_arm_sts.steel_set_stats))
    balder_set = create_armor_set("Balder", create_armor_pieces(dt_arm_sts.balder_set_stats))

    steel_set.compare_armor_sets(balder_set)


if __name__ == "__main__":
    main()
