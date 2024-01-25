# print("Hello, world!!!")

def calculate_area(length, width):
    # Calculates the area of a rectangle
    area = length * width
    return area

def get_user_info():
    while True:
        age = input("Enter your age: ")
        try:
            age = int(age)
            if 18 <= age < 65:
                print("You are an adult.")
            elif age >= 65:
                print("You are eligible for senior citizen discounts.")
            else:
                print("You are a minor.")
            break
        except ValueError:
            print("Invalid age. Please enter a number.")

def main():
    # Main function
    length = 10
    width = 5
    area = calculate_area(length, width)
    print("The area is:", area)
    get_user_info()

if __name__ == "__main__":
    main()
