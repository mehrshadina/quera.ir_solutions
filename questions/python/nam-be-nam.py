def findd(names_list, initial_letter='', cache={}):
    state_key = (tuple(names_list), initial_letter)
    if state_key in cache:
        return cache[state_key]

    max_chain = []

    for current_name in names_list:
        if current_name.startswith(initial_letter):
            remaining_names = []
            for name in names_list:
                if name != current_name:
                    remaining_names.append(name)
            next_initial = current_name[-1]
            current_chain = [current_name] + findd(remaining_names, next_initial, cache)
            if len(current_chain) > len(max_chain):
                max_chain = current_chain

    cache[state_key] = max_chain
    print(', '.join(max_chain))

input_names = input().split(', ')
sorted_names = sorted(input_names)

findd(sorted_names)

