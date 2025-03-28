import math

users = set()

invoices = {}

def create_user(email: str):
    if email in users:
        text = "User already exists!"
        return text
    else:
        users.add(email)
        invoices[email] = []
        text = "User created!"
        return text

def get_users_set():
    return users

def add_bill(email, due, value):
    if email not in users:
        text = "User doesn't exist!"
        return text
    if value <= 0:
        text = "Invalid value!"
        return text
    invoices[email].append({"due": due, "value": value})
    text = "Bill added successfully!"
    return text

def get_users_bills(email):
    if email not in users:
        text = "User doesn't exist!"
        return text
    return invoices[email]

def calculate_bills_props(email):
    if email not in users:
        text = "User doesn't exist!"
        return text
    
    user_invoices = invoices[email]
    if not user_invoices:
        dic = {"sum": 0, "avg": 0, "stddev": 0}
        return dic

    values = []
    for bill in user_invoices:
        values.append(bill["value"])
    
    total = sum(values)
    avg = total / len(values)
    
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    stddev = math.sqrt(variance)
    
    dic = {"sum": total, "avg": avg, "stddev": stddev}
    return dic
