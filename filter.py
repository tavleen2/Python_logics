def is_greater_than(x):
    if x>9:
        return True
    else:
        return False
    
num = [2,4,2,4,2,4,2,3,33,22,52,52]

new = list(filter(is_greater_than, num))
print(new)