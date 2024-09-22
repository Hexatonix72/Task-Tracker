from enum import Enum

class MyClass:
    class Options(Enum):
        OPTION1 = "option1"
        OPTION2 = "option2"
        OPTION3 = "option3"

    def __init__(self, option):
        if not isinstance(option, self.Options):
            raise ValueError("Invalid option")
        self.option = option

# Usage
obj1 = MyClass(MyClass.Options.OPTION1)
print(obj1.option)  # Output: Options.OPTION1