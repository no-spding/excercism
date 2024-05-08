"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args: int) -> list:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *list_of_wagons, = *args,
    return list_of_wagons


def fix_list_of_wagons(each_wagons_id: list, missing_wagons: list) -> list:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    new_wagon_1, new_wagon_2, locomotive, *the_rest = each_wagons_id
    *new_train, = locomotive, *missing_wagons, *the_rest, new_wagon_1, new_wagon_2
    return new_train


def add_missing_stops(route: dict, **kwargs: str) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    *stops, = kwargs.values()
    return {**route, "stops" : stops}


def extend_route_information(route: dict, more_route_information: dict) -> dict:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows:list) -> list:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [*row_one], [*row_two], [*row_three] = zip(*wagons_rows)
    return [row_one, row_two, row_three]