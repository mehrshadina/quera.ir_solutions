from decimal import Decimal
import ast

country_currencies = {
    "IRT": int(1), "USD": int(59700),
    "TRY": int(1845), "EUR": int(64550),
    "GBP": int(75800), "CHF": int(66450),
    "CAD": int(43350),
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        result = "{} {}".format(self.amount, self.currency)
        return result
    
    def __str__(self):
        result = "{} {}".format(self.amount, self.currency)
        return result

    def to_irt(self):
        a = self.amount
        b = country_currencies[self.currency]
        cross = a * b
        return cross

    def from_irt(self, amount_irt, target_currency):
        a = amount_irt
        b = country_currencies[target_currency]
        c = a/b
        return c
    
    def __add__(self, other):
        if isinstance(other, Money):
            a = self.to_irt()
            b = other.to_irt()
            c = a + b 
            result = Money(self.from_irt(c, self.currency), self.currency)
            return result
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            a = self.to_irt()
            b = other.to_irt()
            c =  a - b
            result = Money(self.from_irt(c, self.currency), self.currency) 
            return result
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Money(self.amount * other, self.currency)
            return result
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Money):
            a = self.to_irt()
            b = other.to_irt()
            c = a / b
            return c
        
        elif isinstance(other, (int, float)):
            result = Money(self.amount / other, self.currency) 
            return result
        
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, Money):
            a = self.to_irt()
            b = other.to_irt()
            c = a // b
            return c
        elif isinstance(other, (int, float)):
            result = Money(self.amount // other, self.currency) 
            return result
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money):
            a = self.to_irt()
            b = other.to_irt()
            result = a < b
            return result
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Money):
            a = self.to_irt()
            b = other.to_irt()
            result = a <= b
            return result
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Money):
            a = self.to_irt()
            b = other.to_irt()
            result = a > b
            return result
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Money):
            a = self.to_irt()
            b = other.to_irt()
            result = a >= b
            return result
        return NotImplemented

    def convert(self, target_currency):
        amount_in_irt = self.to_irt()
        converted_amount = self.from_irt(amount_in_irt, target_currency)
        result = Money(converted_amount, target_currency)
        return result

def main():
    context = {
        "Money": Money, 
        "Decimal": Decimal, 
        "sorted": sorted, 
        "sum": sum
    }
    
    loop_numbers = int(input())
    for _ in range(loop_numbers):
        user_input = input()
        result = eval(compile(ast.parse(user_input, mode='eval'), filename="<ast>", mode="eval"), context)
        print(result)


main()
