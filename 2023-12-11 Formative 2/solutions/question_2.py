def common_values(lst1: list, lst2: list) -> list:
    """Takes two lists and returns a list containing items common between the two

    Args:
        lst1 (list): List 1
        lst2 (list): List 2

    Returns:
        list: A list containing items common between lst1 and lst2
    """
    common_items = []

    for item in lst1:
        if item in lst2 and item not in common_items:
            common_items.append(item)

    return common_items
