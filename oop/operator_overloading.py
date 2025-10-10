class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x +p.x), (self.y +p.y))  #returning a new point object
    
    def print_point(self):
        print(f"X is {self.x} and y is {self.y}")

    def __add__(self,p):
        return Point((self.x +p.x), (self.y +p.y))

p1 = Point(3,2)
p2 = Point(7,3)

# p = p1.sum(p2)  #this will return a new point object but we are not storing it anywhere
p = p1+p2 #I overloaded the + operator with __add__ to do the same thing as sum method
p.print_point()