# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))

#         print(f"The sum is {a+b}")

#     except ValueError:
#         print("Please do not perform  badtypecaste")

#     except ZeroDivisionError:
#         print("Please do not divide by zero")

#     except Exception as e:
#         print("ERROR!!", e)

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")

# Alternative using a tuple:
try:
  num = int(input("Enter a number: "))
  result = 10 / num
except (ZeroDivisionError, ValueError) as e:
  print(f"An error occurred: {e}")