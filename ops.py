def add(x: float, y: float) -> float:
    """Returns the sum of x and y."""
    return x+y

def subtract(x: float, y: float) -> float:
    """Returns the difference of x and y."""
    return x-y

def multiply(x: float, y: float) -> float:
    """Returns the product of x and y."""
    return x*y

def divide(x: float, y: float) -> float:
    """Returns the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y