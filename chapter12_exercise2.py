##
# CIS 117 - Chapter 12 Exercise 2 - Erick Ramos
#
# This program creates the Fibonacci numbers
# using both an iterator and a generator.
# The max limit is set with the FIBONACCI_LIMIT variable
#


FIBONACCI_LIMIT = 8


class Fibonacci:
    """ Iterator to generate Fibonacci numbers """
    def __init__(self, limit):
        self.previous = 0
        self.current = 1
        self.count = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        else:
            value = self.current

        # Tuple unpacking to udpate values correctly
            self.previous, self.current = self.current, self.previous + self.current
            self.count += 1
            return value


def fibonacci_generator(limit):
    """ Generator that uses the Fibonacci class to yield values """
    for value in Fibonacci(limit):
        yield value



if __name__ == "__main__":
    print("Fibonacci iterator:")
    fibonacci_iterator = Fibonacci(FIBONACCI_LIMIT)
    for number in fibonacci_iterator:
        print(number, end=" ")

    print("\n\nFibonacci generator:")
    for number in fibonacci_generator(FIBONACCI_LIMIT):
        print(number, end=" ")


## Output 1
# Fibonacci iterator:
# 1 1 2 3 5 8 13 21 

# Fibonacci generator:
# 1 1 2 3 5 8 13 21 

## Output 2
# Fibonacci iterator:
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 

# Fibonacci generator:
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711