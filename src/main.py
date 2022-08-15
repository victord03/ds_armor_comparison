from classes.armor_set import ArmorSet
from data.armor_sets import armor_sets


def main():

    # todo: automated the instantiation from the data file
    balder_set = ArmorSet(armor_sets["balder_set"])
    steel_set = ArmorSet(armor_sets["steel_set"])
    chain_set = ArmorSet(armor_sets["chain_set"])
    black_iron_set = ArmorSet(armor_sets["black_iron_set"])

    print(balder_set)
    print(steel_set)
    print(chain_set)
    print(black_iron_set)

    # list_of_armor_sets = [steel_set, chain_set]
    # brute_score = steel_set.compare_armor_set(list_of_armor_sets)
    # print(brute_score)


if __name__ == "__main__":
    main()
