import math


def track_points(
        time: float,
        event_parameters: tuple[float, float, float]) -> int:
    """Calculate the points scored by an athlete with the given time
    and parameters and return the points as an int

    Args:
        time (float): The time taken
        event_parameters (tuple[float, float, float]): Event parameters

    Raises:
        ValueError: Thrown if event_parameters does not have exactly 
        three values.

    Returns:
        int: The number of points scored by the athlete, 0 if negative.
    """
    # Raise a ValueError if the length of
    # event_parameters isn't exactly 3
    if len(event_parameters) != 3:
        raise ValueError

    # Separate out the parameters to avoid repeated indexing
    param_a = event_parameters[0]
    param_b = event_parameters[1]
    param_c = event_parameters[2]

    # Return 0 if b - time is less than 0
    if param_b < time:
        return 0

    # Carry out the points calculation
    points = param_b - time
    points = pow(points, param_c)
    points = points * param_a

    # Round the points down to the nearest integer
    points = math.floor(points)

    # Return the points vae
    return points
