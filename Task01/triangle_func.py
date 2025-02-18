class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
    """
    >>> get_triangle_type(2, 2, 2)
    'equilateral'
    >>> get_triangle_type(2, 3, 4)
    'nonequilateral'
    >>> get_triangle_type(2, 2, 3)
    'isosceles'
    >>> get_triangle_type(1, 2, 5)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides
    >>> get_triangle_type(-1, 2, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides
    """
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"

#print(get_triangle_type(-1, 2, 3))
