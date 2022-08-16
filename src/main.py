from data.armor_sets import armor_sets
from utils.automation import instantiate_all_armors
from utils.comparison import compare_armor_sets as cas, maximize_this_resistance as mr
from utils import ui


def main():

    all_armors_dict = instantiate_all_armors(armor_sets)

    armor_set_a = all_armors_dict["balder_set"]
    armor_set_b = all_armors_dict["chain_set"]

    eval_dict = cas(armor_set_a, armor_set_b)
    print(eval_dict)

    resistance = "lightning"
    # needs fixing after update
    max_res = mr(armor_set_a, armor_set_b, resistance)
    print(ui.display_maximize_dict(max_res, resistance))


if __name__ == "__main__":
    main()
