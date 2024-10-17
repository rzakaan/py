class Example():
    state = (3, str)
    number = (1, int)
    val = (1, bool)

def getattr(cls):
    print(cls)
    for attribute, value in cls.__dict__.items():
        if "__" not in attribute:
            print(attribute, '=', value)

getattr(Example)
print(Example.state)