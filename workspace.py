# class Cookie:
#     def __init__(self, shape, topping):
#         self.shape = shape # shape attribute
#         self.topping = topping
    
#     def print_info(self):
#         print("This is a cookie shaped like a {self.shape} with topping {self.topping}") #formatted string literals, interpolation, found at https://docs.python.org/3/tutorial/inputoutput.html


# star_cookie = Cookie("star", "chocolate chips")
# star_cookie.print_info()

# snowman_cookie = Cookie("snowman", "chocolate chips")
# snowman_cookie.print_info()


# class Car:
#     def __init__(self, color, make): # Constructor, self parameter is a reference to the current instance of the class
#         self.color = color  #  attribute
#         self.make = make    #  attribute

# car_red_toyato = Car("red", "Toyota") # Instance of Car class with color attribute set to red, and make attribute set to Toyota
# print(car_red_toyato.color)  # Output: red

# car_blue_ford = Car("blue", "Ford") # Instance of Car class with color attribute set to blue, and make attribute set to Ford
# print(car_blue_ford.make)   # Output: Ford

# More info on Classes in Python Documentation: https://docs.python.org/3/tutorial/classes.html 
# More info on Classes vs Instances: https://www.geeksforgeeks.org/python-attributes-class-vs-instance-explained/

# for x in range(0, 3): # 0 indexing, starts at 0, ends with 2
#     print(f"Now we're on {x}")

for a in range(0, 3):
    print(a)