class Calculator:

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b

    def is_prime_number(self, n):
        if n < 2:
            return False

        if n == 2:
            return True
        if n % 2 == 0:
            return False

        limit = int(n ** 0.5) + 1
        for divisor in range(3, limit, 2):
            if n % divisor == 0:
                return False

        return True
