class Money:
    money_rates = {
        "EUR": 64550,
        "CHF": 66450,
        "GBP": 75800,
        "CAD": 43350,
        "USD": 59700,
        "IRT": 1,
        "TRY": 1845
    }

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    @classmethod
    def from_base(cls, amount_base, base_currency):
        answer = cls(amount_base / cls.money_rates[base_currency], base_currency)
        return answer

    def to_base(self):
        answer = self.amount * self.money_rates[self.currency]
        return answer

    def convert(self, target_currency):
        amount_base = self.to_base()
        end = Money.from_base(amount_base, target_currency)
        return end

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Money):
            total_base = self.to_base() + other.to_base()
            return Money.from_base(total_base, self.currency)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            total_base = self.to_base() - other.to_base()
            return Money.from_base(total_base, self.currency)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Money):
            return self.to_base() / other.to_base()
        elif isinstance(other, (int, float)):
            return Money(self.amount / other, self.currency)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, Money):
            return self.to_base() // other.to_base()
        elif isinstance(other, (int, float)):
            return Money(self.amount // other, self.currency)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.to_base() == other.to_base()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.to_base() < other.to_base()
        return NotImplemented

for _ in range(int(input())):
    print(eval(input()))

