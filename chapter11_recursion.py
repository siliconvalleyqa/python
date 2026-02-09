##
# CIS 117 - Chapter 11 Exercise Recursion - Erick Ramos
#
# Given a class Rectangle with instance variables width and height. 
# provide a recursive getArea method. 
# Construct a rectangle whose width is one less than the original and call its getArea method.
#

class Rectangle:
    """ A class representing a rectangle.
        Attributes:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """ Initializes a Rectangle instance.
            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def getArea(self):
        """
        Recursively calculates the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        # Base case: If width or height is 0, the area is 0
        if self.width == 0 or self.height == 0:
            return 0
        
        # Base case: if width is 1, area is simply height
        if self.width == 1:
            return self.height
        
        if self.height == 1:
            return self.width

        # Recursive case: break rectangle into one column + smaller rectangle
        smaller_rectangle = Rectangle(self.width - 1, self.height)
        return self.height + smaller_rectangle.getArea()


# Test the recursive method
rectangle = Rectangle(3, 4)
the_area = rectangle.getArea()
print("Expected: 12, Actual:", the_area)


# Test the recursive method
rectangle2 = Rectangle(0, 0)
the_area2 = rectangle2.getArea()
print("Expected: 0, Actual:", the_area2)


## Output 1
# Expected: 12, Actual: 12

## Output 2
# Expected: 0, Actual: 0
