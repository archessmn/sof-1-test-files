import os


def read_from_file(filename: str) -> dict:
    """Takes the name of a file, reads it and parses its data,
    returns a dict with keys as athletes names and the values 
    the athletes times

    Args:
        filename (str): The name of the file to read

    Raises:
        ValueError: Raised if the number of fields on a line in the
        file is incorrect
        ValueError: Raised if one of the fields provided as a time
        cannot be parsed as a float

    Returns:
        dict: A dictionary containing athletes times with the keys as
        their names
    """
    # Open the given file and read its contents
    with open(filename) as file:
        lines = file.readlines()

    # Declare the dictionary to write data to
    output_dict = {}

    for line in lines:
        if line.startswith("#"):
            # Ignore line as it is a comment
            continue
        else:
            fields = line.split(", ")

            # Raise a ValueError if there is an incorrect number of fields
            if len(fields) != 4:
                raise ValueError(
                    f"Bad number of fields line: {lines.index(line)}")

            # Attempt to parse times and add to the dict
            # Raises a value error if the data can't be parsed
            try:
                output_dict[fields[0]] = {
                    '200m': float(fields[1]),
                    '110m': float(fields[2]),
                    '800m': float(fields[3])
                }
            except:
                raise ValueError("Unable to parse data")

    return output_dict


# print(read_from_file("SOF1-EvenYears-Formative2-sourcefiles/data/correctDataFormat.txt"))
