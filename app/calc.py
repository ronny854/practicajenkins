import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def sqrt(self, x):
        self.check_types_math(x)
        return math.sqrt(x)

    def log10(self, x):
        self.check_types_math(x)
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

    def check_types_math(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameters must be numbers(int o float).")    

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    result2 = calc.sqrt(25)
    result3 = calc.log10(100)
    print(result)
    print("result sqrt 25 = "+str(result2))
    print("result log10 100 = "+str(result3))