from classes.armor_set import ArmorSet


def instantiate_all_armors(armor_set_data: dict) -> dict:
    """Runs at the beginning of the file, to instantiate all armor sets in a
    dict named 'all_armor_instances'."""

    all_armor_instances = {}

    for armor_set_name, armor_set_bulk in armor_set_data.items():

        all_armor_instances[armor_set_name] = ArmorSet(armor_set_bulk)

    return all_armor_instances
