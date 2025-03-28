import re

input_text = input()
emails = re.findall('([a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{3,})', input_text)

if len(emails) == 0:
    print('empty')
else:
    for email in emails:
        print(email)

