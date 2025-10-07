# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))

# if b==0:
#     raise ValueError("Please do not divide by zero")

# print(f"The division is {a/b}")

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return "Access granted."
 
try:
  print(check_age(20))  # Access granted.
  print(check_age(16))  # Raises ValueError
except ValueError as e:
  print(f"Error: {e}")