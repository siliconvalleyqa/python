##
# CIS 117 - Chapter 9 Exercise 1 - Erick Ramos
#
# "Chapter 9 - Assignment": P9.12
# Write a class Bug that models a bug moving along a horizontal line. The bug moves
# either to the right or left. Initially, the bug moves to the right, but it can turn to
# change its direction. In each move, its position changes by one unit in the current
# direction. Provide a constructor
#     def _ _init_ _(self, initialPosition)
# and methods
# - def turn(self)
# - def move(self)
# - def getPosition(self)

# Sample usage:
#     bugsy = Bug(10)
#     bugsy.move() # Now the position is 11
#     bugsy.turn()
#     bugsy.move() # Now the position is 10
# Your driver program should construct a bug, make it move and turn a few times, and
# print the actual and expected positions.
#

class Bug:

    def __init__(self, initialPosition):
        self._position = initialPosition
        self._direction = 1 # Initiall the bug moves to the right

    def turn(self):
        self._direction = self._direction * -1

    def move(self):
        self._position = self._position + self._direction

    def getPosition(self):
        return self._position
    
def main():
    bugsy = Bug(10)
    bugsy.move() # Now the position is 11
    print("Expected: 11, Actual:", bugsy.getPosition())
    bugsy.turn()
    bugsy.move() # Now the position is 10
    print("Expected: 10, Actual:", bugsy.getPosition())

    firebug = Bug(69)
    for i in range(597):
        firebug.move()
    print("Expected: 666, Actual:", firebug.getPosition())

    firebug.turn()
    for i in range(1332):
        firebug.move()
    print("Expected: -666, Actual:", firebug.getPosition())


if __name__ == "__main__":
    main()



## Output 1
# Expected: 11, Actual: 11
# Expected: 10, Actual: 10

## Output 2
# Expected: 666, Actual: 666
# Expected: -666, Actual: -666