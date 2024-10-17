def list_comprehension():
    """
        List comprehension is a Pythonic way to create lists with a single line of code

    """

    # using a traditional loop
    squared_numbers = []
    for i in range(10):
        squared_numbers.append(i ** 2)

    # list comprehension
    squared_numbers = [i ** 2 for i in range(10)]


def lambda_function():
    # traditional way
    def add(x, y): return x + y

    # lambda way
    # addl = lambda x, y: x + y


def map_filter_reduce():
    """
        map
        filter
        reduce
    """
    fruits = ['apple', 'banana', 'cherry']

    # traditional way
    upper_case_fruits = []
    for f in fruits:
        upper_case_fruits.append(f.upper())

    # map way
    upper_case_fruits = list(map(lambda f: f.upper(), fruits))


def ternary_operator():
    """ 
        The ternary operator provides a condensed way to write conditional statements in a single line
    """

    # traditional way
    result = None
    num = 5
    if num % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    # ternary operator
    result = "Event" if num % 2 == 0 else "Odd"


def zip_function():
    students = ['Aa', 'Bb', 'Cc', 'Dd']
    grades = [10, 20, 30, 40]

    # traditional way
    pairs = []
    for i in range(len(students)):
        pairs.append((students[i], grades[i]))

    # zip functions
    pairs = list(zip(students, grades))


def enumerate_function():
    fruits = ['banana', 'apple', 'cherry']

    # traditional way
    for i in range(len(fruits)):
        print(f"{i}. {fruits[i]}")

    # enumerate
    for idx, f in enumerate(fruits):
        print("{}: {}".format(idx + 1, f))


def join_function():
    words = ['Python', 'is', 'awesome', 'and', 'powerful']
    sentence = ''

    # traditional way
    for word in words:
        sentence += word + ' '

    # using .join() method
    sentence = ' '.join(words)


def unpacking_list():
    nums = [1, 2, 3]
    x, y, z = nums
