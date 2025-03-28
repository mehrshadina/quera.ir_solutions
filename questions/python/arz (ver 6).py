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

    def to_irt(self):
        return self.amount * rates[self.currency]

    def from_irt(self, amount_irt, target_currency):
        return amount_irt / rates[target_currency]

    def convert(self, target_currency):
        amount_in_irt = self.to_irt()
        converted_amount = self.from_irt(amount_in_irt, target_currency)
        return Money(converted_amount, target_currency)

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __str__(self):
        return f"{self.amount} {self.currency}"

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

# Sample Input/Output Handling
for _ in range(int(input())):
    print(eval(input()))
