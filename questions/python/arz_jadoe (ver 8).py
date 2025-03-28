from decimal import Decimal
import ast

country_currencies = {
    "IRT": int(1), "USD": int(59700), "TRY": int(1845), "EUR": int(64550), "GBP": int(75800), "CHF": int(66450), "CAD": int(43350),
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

    def iran_tooman(self):
        amount = self.amount
        currency = country_currencies[self.currency]
        return amount * currency

    def from_irt(self, amount_irt, target_currency):
        amount = amount_irt
        currency = country_currencies[target_currency]
        return amount / currency
    
    def __add__(self, other):
        if isinstance(other, Money):
            ir_tooman = self.iran_tooman()
            foreign = other.iran_tooman()
            return Money(self.from_irt(foreign + ir_tooman, self.currency), self.currency)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            ir_tooman = self.iran_tooman()
            foreign = other.iran_tooman()
            return Money(self.from_irt(ir_tooman - foreign, self.currency), self.currency) 
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Money):
            ir_tooman = self.iran_tooman()
            foreign = other.iran_tooman()
            return ir_tooman / foreign
        
        elif isinstance(other, (int, float)):
            return Money(self.amount / other, self.currency) 
        
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, Money):
            ir_tooman = self.iran_tooman()
            foreign = other.iran_tooman()
            return ir_tooman // foreign
        elif isinstance(other, (int, float)):
            return Money(self.amount // other, self.currency) 
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money):
            ir_tooman = self.iran_tooman()
            foreign = other.iran_tooman()
            return ir_tooman < foreign
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Money):
            ir_tooman = self.iran_tooman()
            foreign = other.iran_tooman()
            return ir_tooman <= foreign
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Money):
            ir_tooman = self.iran_tooman()
            foreign = other.iran_tooman()
            return ir_tooman > foreign
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Money):
            ir_tooman = self.iran_tooman()
            foreign = other.iran_tooman()
            return ir_tooman >= foreign
        return NotImplemented

    def convert(self, target_currency):
        amount_in_irt = self.iran_tooman()
        converted_amount = self.from_irt(amount_in_irt, target_currency)
        result = Money(converted_amount, target_currency)
        return result


count = int(input())
for _ in range(count):
    job = ast.parse(input(), mode='eval')
    job = eval(compile(job, filename="<ast>", mode="eval"), {
    "Money": Money, 
    "Decimal": Decimal, 
    "sorted": sorted, 
    "sum": sum
})
    print(job)



