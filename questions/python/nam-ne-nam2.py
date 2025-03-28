def next_words(names, start_with):
    competibles = [name for name in names if name.startswith(start_with)]
    return competibles

def new_names(names, excepted):
    return names.remove(excepted)

def longest_chain(names, start_letter=None):
    chains = []

    if start_letter is None:
        last_char = ''

    for name in names:
        chains.append([])
        names2 = new_names(names, name)
        for next_name in next_words(names2, last_char):
            chains[-1] = [next_name] + longest_chain(new_names(names, name), last_char)


names = input().split(', ')
for start_letter in set([x[0] for x in names]):
    result = longest_chain(names, start_letter=start_letter)
print(', '.join(result))
