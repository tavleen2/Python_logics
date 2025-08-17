marks = [22,44,55,66,78]
mixed = [22, '44', 55, '66', 78]

print(marks)

marks.append(67) #add an element to the end of the list
print(marks)

marks.pop() #remove the last element from the list
print(marks)

marks.insert(2, 99) #insert an element at a specific index
print(marks)

marks.sort() #sort the list in ascending order
print(marks)

marks.extend(mixed) #extend the list with another list
print(marks)

marks.reverse() #reverse the list
print(marks)

marks.remove(44) #remove a specific element from the list
print(marks)