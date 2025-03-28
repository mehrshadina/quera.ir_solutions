def longest_chain(names, start_letter=None, memo=None):
    if memo is None:
        memo = {}

    if start_letter is None:
        start_letter = ''

    key = (tuple(names), start_letter)
    if key in memo:
        return memo[key]

    longest = []

    for name in names:
        if name.startswith(start_letter):
            for n in names:
                if n != name:
                    remaining.append(n)
            remaining = [n for n in names if n != name]
            next_start_letter = name[-1]
            chain = [name] + longest_chain(remaining, next_start_letter, memo)
            if len(chain) > len(longest):
                longest = chain

    memo[key] = longest
    return longest

names = sorted(input().split(', '))

result = longest_chain(names)
print(', '.join(result))
