from classes.project_classes import ArmorSet
import data.armor_sets as dt_arm_sts


def main():

    balder_set = ArmorSet(dt_arm_sts.balder_set)
    steel_set = ArmorSet(dt_arm_sts.steel_set)
    chain_set = ArmorSet(dt_arm_sts.chain_set)

    # print(balder_set)
    # print(steel_set)
    # print(chain_set)

    # balder_set.compare_armor_sets(steel_set)


if __name__ == "__main__":
    main()
