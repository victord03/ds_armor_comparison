from classes.project_classes import ArmorSet
import data.armor_sets as dt_arm_sts


def main():

    # todo: automated the instantiation from the data file
    balder_set = ArmorSet(dt_arm_sts.balder_set)
    steel_set = ArmorSet(dt_arm_sts.steel_set)
    chain_set = ArmorSet(dt_arm_sts.chain_set)
    black_iron_set = ArmorSet(dt_arm_sts.black_iron_set)

    # print(balder_set)
    # print(steel_set)
    # print(chain_set)

    brute_score = steel_set.compare_armor_set(black_iron_set)
    print(brute_score)


if __name__ == "__main__":
    main()
