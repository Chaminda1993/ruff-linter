def calculate_area(length, width):  # Missing docstring
  area = length * width  # Unclear variable name
  return area  # Implicit return statement

def get_user_info():
  while True:  # Infinite loop without clear exit condition
    try:
      age = int(input("Enter your age: "))
      if age >= 18:
        if age >= 65:
          print("You are eligible for senior citizen discounts.")
        else:
          print("You are an adult.")
      else:
        print("You are a minor.")
      break
    except ValueError:
      print("Invalid age. Please enter a number.")
      continue

def process_data(data_list):
  for item in data_list:
    if item == "":  # Empty string check
      continue  # Empty block
    elif isinstance(item, int) and item > 10 or isinstance(item, str) and item.startswith("a"):
      print(item)

# Long function with multiple responsibilities
def manage_employee_records():
  # ... code for adding, removing, and updating employee records ...

# Global variable
global_counter = 0

# Unused import
import math

# Dead code
def unused_function():
  print("This function is never called.")

# Long parameter list
def send_notification(user_id, email, phone_number, message, priority=False, include_attachments=True):
  # ... code to send notification ...

# Code with multiple code smells combined
def complex_task():
  for i in range(100):
    if i % 2 == 0:
      try:
        result = some_function(i)  # Undeclared function
      except Exception as e:  # Broad exception handling
        print("An error occurred:", e)