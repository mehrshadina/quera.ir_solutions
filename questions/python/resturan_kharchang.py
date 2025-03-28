def find_derivative(expression):
    def derivative_term(term):
        if term == "0" or "*" not in term: 
            return "0"
        coefficient, power_str = term.split("*")
        if "^" not in power_str: 
            return coefficient
        power = int(power_str.split("^")[1])
        new_coefficient = int(coefficient) * power
        new_power = power - 1
        if new_power == 0:
            return str(new_coefficient)
        if new_coefficient == 0: 
            return "0" 
        return f"{new_coefficient}*X^{new_power}"

    terms = expression.split('+')
    derivative_terms = [derivative_term(term) for term in terms]
    derivative_expression = '+'.join(derivative_terms)
    derivative_expression = derivative_expression.lstrip('+').rstrip('0') 
    return derivative_expression or "0", "EVEN" if all(int(term.split('*')[-1].split('^')[1]) % 2 == 0 for term in derivative_expression.split('+') if '^' in term) else "ODD"

expression = input()
derivative, parity = find_derivative(expression)
print(derivative)
print(parity)