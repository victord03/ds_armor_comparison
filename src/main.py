from data.armor_sets import armor_sets
from utils.automation import instantiate_all_weapons
from utils.comparison import compare_armor_sets as cas, maximize_this_resistance as mr
from utils import ui


def main():

    all_weapons_dict = instantiate_all_weapons(armor_sets)

    armor_set_a = all_weapons_dict["balder_set"].__dict__
    armor_set_b = all_weapons_dict["steel_set"].__dict__

    eval_dict = cas(armor_set_a, armor_set_b)

    resistance = "lightning"
    max_res = mr(armor_set_a, armor_set_b, resistance)
    print(ui.display_maximize_dict(max_res, resistance))


if __name__ == "__main__":
    main()
