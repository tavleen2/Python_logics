#without walrus operator
data = input("Enter a value (or 'quit' to exit): ")
while data != "quit":
    print(f"You entered: {data}")
    data = input("Enter a value( or 'quit' to exit): ")

#with walrus operator
while(data :=input("Enter a value (or 'quit' to exit: "))!="quit":
    print(f"You entered:{data}")