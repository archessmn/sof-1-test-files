def check_level(level: list[int], start=-1) -> bool:
    """Takes in a list of positive integers describing a game level
    and checks if the level is possible to complete, returning
    a boolean with the result.

    I know how it works and wrote it all intentionally in an attempt
    to make a fully recursive solution. It passes the tests I have
    used on it including some not given which I know the result for,
    however it is far from a fully functional solution.

    Args:
        level (list[int]): A list containg positive integers 
        describing a game level
        start (int, optional): Start pointer used only when the
        function is recursing. Defaults to -1 and shouldn't be set
        otherwise.

    Returns:
        bool: The result of the testing whether or not the level is
        feasable
    """
    # If the level check starts on itself,
    # check from the next item instead
    if start == 0:
        return check_level(level[1:])

    # Assign the value of start, used for the function to know where
    # in the list it should start calling check_level from
    if start != -1:
        level[0] = start
    else:
        start = level[0]

    # If there is one node left and it isn't 0 return True
    if len(level) == 1 and level[0] != 0:
        return True

    # If the start node is greater than the length of the level,
    # decrease the value of the start node on the next run
    if start > len(level) - 1:
        return check_level(level=level, start=start - 1)

    # If the level starts with a 0, check if it was
    # intentional game design or caused by the function
    if level[start] == 0:
        # Check if the 0 was there originally
        if start == 0:
            return False
        # Else continue checking
        return check_level(level=level, start=start - 1)
    else:
        # Check if the level can succeed from after the start pointer
        if check_level(level[start:]):
            return True
        # Otherwise move the start pointer back
        return check_level(level=level, start=start - 1)
