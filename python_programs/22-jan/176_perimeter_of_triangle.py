def get_perimeter(side1: int, side2: int, side3: int) -> int:
    '''
    this function inputs all the sides of triangle and return perimeter of it.
    
    :param side1: first side of triangle
    :type side1: int
    :param side2: Second side of triangle
    :type side2: int
    :param side3: Third side of triangle
    :type side3: int
    :return: Perimeter of triangle
    :rtype: int
    '''

    return side1 + side2 + side3


print(get_perimeter(4, 5, 6))