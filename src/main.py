from data.armor_sets import armor_sets
from utils.automation import instantiate_all_weapons
from utils.comparison import compare_armor_sets as cas


def main():

    all_weapons_dict = instantiate_all_weapons(armor_sets)

    armor_set_a = all_weapons_dict["chain_set"].__dict__
    armor_set_b = all_weapons_dict["steel_set"].__dict__

    eval_dict = cas(armor_set_a, armor_set_b)
    print(eval_dict)


if __name__ == "__main__":
    main()
