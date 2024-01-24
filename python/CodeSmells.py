"""Calculates the area of a rectangle and validates user input."""

def calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If either length or width is negative.
    """

    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative values.")

    return length * width

def get_rectangle_dimensions():
    """Prompts the user for rectangle dimensions and validates input.

    Returns:
        tuple: A tuple containing the validated length and width.
    """

    while True:
        try:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            return length, width
        except ValueError:
            print("Invalid input. Please enter numerical values for length and width.")

if __name__ == "__main__":
    """Main execution block."""

    length, width = get_rectangle_dimensions()
    area = calculate_rectangle_area(length, width)
    print("The area of the rectangle is:", area)
