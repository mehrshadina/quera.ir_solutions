class Money:
    base_currency = "IRT"
    rates = {
        "IRT": 1,
        "TRY": 1845,
        "USD": 59700,
        "CHF": 66450,
        "CAD": 43350,
        "EUR": 64550,
        "GBP": 75800,
    }

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def to_base_currency(self):
        return self.amount * self.rates[self.currency]

    def from_base_currency(self, amount_base, target_currency):
        return amount_base / self.rates[target_currency]

    def convert(self, target_currency):
        return Money(self.from_base_currency(self.to_base_currency(), target_currency), target_currency)

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Money):
            total_base = self.to_base_currency() + other.to_base_currency()
            return Money(self.from_base_currency(total_base, self.currency), self.currency)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            total_base = self.to_base_currency() - other.to_base_currency()
            return Money(self.from_base_currency(total_base, self.currency), self.currency)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Money):
            return self.to_base_currency() / other.to_base_currency()
        elif isinstance(other, (int, float)):
            return Money(self.amount / other, self.currency)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, Money):
            return self.to_base_currency() // other.to_base_currency()
        elif isinstance(other, (int, float)):
            return Money(self.amount // other, self.currency)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.to_base_currency() < other.to_base_currency()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Money):
            return self.to_base_currency() <= other.to_base_currency()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Money):
            return self.to_base_currency() > other.to_base_currency()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Money):
            return self.to_base_currency() >= other.to_base_currency()
        return NotImplemented

for _ in range(int(input())):
    print(eval(input()))
