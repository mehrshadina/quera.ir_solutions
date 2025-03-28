from decimal import Decimal, getcontext
import ast

# Set the precision for Decimal to 15
getcontext().prec = 15

rates = {
    "IRT": 1,
    "USD": 59700,
    "EUR": 64550,
    "GBP": 75800,
    "CHF": 66450,
    "CAD": 43350,
    "TRY": 1845
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def to_irt(self):
        return self.amount * rates[self.currency]

    def from_irt(self, amount_irt, target_currency):
        return amount_irt / rates[target_currency]

    def __add__(self, other):
        if isinstance(other, Money):
            total_irt = self.to_irt() + other.to_irt()
            return Money(self.from_irt(total_irt, self.currency), self.currency)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            total_irt = self.to_irt() - other.to_irt()
            return Money(self.from_irt(total_irt, self.currency), self.currency)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Money):
            return self.to_irt() / other.to_irt()
        elif isinstance(other, (int, float)):
            return Money(self.amount / other, self.currency)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, Money):
            return self.to_irt() // other.to_irt()
        elif isinstance(other, (int, float)):
            return Money(self.amount // other, self.currency)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.to_irt() < other.to_irt()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Money):
            return self.to_irt() <= other.to_irt()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Money):
            return self.to_irt() > other.to_irt()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Money):
            return self.to_irt() >= other.to_irt()
        return NotImplemented

    def convert(self, target_currency):
        amount_in_irt = self.to_irt()
        converted_amount = self.from_irt(amount_in_irt, target_currency)
        return Money(converted_amount, target_currency)

def safe_eval(expr, context):
    try:
        # Parse the expression into an AST
        tree = ast.parse(expr, mode='eval')
        # Compile and evaluate the AST
        code = compile(tree, filename="<ast>", mode="eval")
        return eval(code, context)
    except Exception as e:
        return f"Error evaluating expression: {e}"

def main():
    context = {"Money": Money, "Decimal": Decimal, "sorted": sorted, "sum": sum}
    
    try:
        how_many_calc = int(input())
    except ValueError:
        print("Invalid number")
        return

    for _ in range(how_many_calc):
        user_input = input()
        result = safe_eval(user_input, context)
        print(result)

if __name__ == "__main__":
    main()
