def parabola_focus(a, b, c):
    """
    Calculate the focus of a parabola y = ax^2 + bx + c.

    Args:
        a (float): Coefficient of x^2
        b (float): Coefficient of x
        c (float): Constant term

    Returns:
        tuple: Coordinates (x, y) of the focus
    """
    if a == 0:
        print("Cannot devide by 0")
        return -1

    h = -b / (2 * a)
    k = c - (b**2) / (4 * a)

    focus_y = k + 1 / (4 * a)
    return (h, focus_y)


a, b, c = 1, -2, 1
focus = parabola_focus(a, b, c)
print(f"Focus: {focus}")
