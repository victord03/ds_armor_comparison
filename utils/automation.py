from classes.armor_set import ArmorSet


def instantiate_all_weapons(armor_set_data: dict) -> dict:

    all_instances = {}

    for armor_set_name, armor_set_bulk in armor_set_data.items():

        all_instances[armor_set_name] = ArmorSet(armor_set_bulk)

    return all_instances
