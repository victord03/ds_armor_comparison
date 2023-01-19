
def display_maximize_dict(maximized: dict, resistance_maximized_for: str) -> str:
    """Function to display the dict returned from the comparison/maximize_this_resistance function
    with explanatory text."""

    text = f"\nBetween the two, use the following combination for maximized {resistance_maximized_for} resistance:"

    for key, value in maximized.items():
        text += f"\n\t{key.upper()}: {value[0]} armor set (+{value[1]})."

    return text + "\n"
