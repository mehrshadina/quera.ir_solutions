rates = {
    "IRT": 1,
    "EUR": 64550,
    "TRY": 1845,
    "USD": 59700,
    "GBP": 75800,
    "CHF": 66450,
    "CAD": 43350,
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

    def from_irt(self, amount_irt, tar):
        return amount_irt / rates[tar]

    def __add__(self, digar):
        if isinstance(digar, Money):
            total_irt = self.to_irt() + digar.to_irt()
            return Money(self.from_irt(total_irt, self.currency), self.currency)
        
        return NotImplemented

    def __sub__(self, digar):
        if isinstance(digar, Money):
            total_irt = self.to_irt() - digar.to_irt()
            return Money(self.from_irt(total_irt, self.currency), self.currency)
        
        return NotImplemented

    def __mul__(self, digar):
        if isinstance(digar, (int, float)):
            return Money(self.amount * digar, self.currency)
        
        return NotImplemented

    def __truediv__(self, digar):
        if isinstance(digar, Money):
            return self.to_irt() / digar.to_irt()
        
        elif isinstance(digar, (int, float)):
            return Money(self.amount / digar, self.currency)
        
        return NotImplemented

    def __floordiv__(self, digar):
        if isinstance(digar, Money):
            return self.to_irt() // digar.to_irt()
        
        elif isinstance(digar, (int, float)):
            return Money(self.amount // digar, self.currency)
        
        return NotImplemented

    def __lt__(self, digar):
        if isinstance(digar, Money):
            return self.to_irt() < digar.to_irt()
        return NotImplemented

    def __le__(self, digar):
        if isinstance(digar, Money):
            return self.to_irt() <= digar.to_irt()
        
        return NotImplemented

    def __gt__(self, digar):
        if isinstance(digar, Money):
            return self.to_irt() > digar.to_irt()
        
        return NotImplemented

    def __ge__(self, digar):
        if isinstance(digar, Money):
            return self.to_irt() >= digar.to_irt()
        
        return NotImplemented

    def convert(self, tar):
        return Money(self.from_irt(self.to_irt(), tar), tar)

count = int(input())
for _ in range(count):
    text = eval(input()) 
    print(text)


