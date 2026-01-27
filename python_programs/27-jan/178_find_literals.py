def find_literals(string, literals):
    """
    This function searches for each literal in the input string and
    records all starting indices where the literal occurs.

    Args:
        string (str): The string in which the literals are searched.
        literals (list[str]): A list of literal strings to search for.

    Returns:
        dict: A dictionary where each key is a literal string and the
              corresponding value is a list of starting indices where
              that literal occurs in the input string.
    """
    result = {}

    for literal in literals:
        positions = []
        start = 0

        while True:
            idx = string.find(literal, start)
            if idx == -1:
                break
            start = idx + 1
            positions.append(idx)
        
        result[literal] = positions

    for key, value in result.items():
        print(f"{key} : {value}")
    return result


string = "This is testing string for testing individual literals."
literals = ["testing", "is", "in", "literal"]

find_literals(string, literals)