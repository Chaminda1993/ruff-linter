def calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle."""
    rectangle_area = length * width
    return rectangle_area

def get_valid_age():
    """Prompts the user for their age and validates input."""
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 <= age <= 120:  # Ensure age is within reasonable range
                return age
            else:
                print("Invalid age. Please enter a number between 0 and 120.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def process_data(data_list):
    """Processes a list of data items."""
    for item in data_list:
        if isinstance(item, int) and item > 10:
            print(item)
        elif isinstance(item, str) and item.startswith("a"):
            print(item)

# Replace manage_employee_records() with smaller, focused functions
# for adding, removing, and updating employee records.
