"""Functions to keep track and alter inventory."""

def create_inventory(items: list) -> dict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    add_items(inventory, items)
    return inventory

def add_items(inventory: dict, items: list) -> dict:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for element in items:
        if element not in inventory:
            inventory[element] = 0
        inventory[element] += 1
    print(inventory)
    return inventory

def decrement_items(inventory: dict, items: list) -> dict:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for element in items:
        if element in inventory and inventory[element] > 0:
            inventory[element] -= 1
    print(inventory)
    return inventory

def remove_item(inventory: dict, item: str) -> dict:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item, inventory)
    print(inventory)
    return inventory

def list_inventory(inventory: dict) -> list:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inv_list = []
    for element, count in inventory.items():
        if count > 0:
            inv_list.append((element, count))
    return inv_list