"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record: tuple) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[-1]


def convert_coordinate(coordinate: str) -> tuple:
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)


def compare_records(azara_record: tuple, rui_record: tuple) -> bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    azara_coord = tuple(azara_record[1])
    rui_coord = rui_record[1]
    return azara_coord == rui_coord

def create_record(azara_record: tuple, rui_record: tuple) -> tuple | str:
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record) == True:
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group: tuple) -> str:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    cleaned_record_group = ""
    for record in combined_record_group:
        temp_list = []
        for item in record:
            if item != record[1]:
                temp_list.append(item)
                temp_tuple = tuple(temp_list)
        cleaned_record_group = cleaned_record_group + str(temp_tuple) + "\n"

    return cleaned_record_group
