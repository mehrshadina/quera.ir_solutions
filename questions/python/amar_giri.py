prepositions = {'a', 'the', 'on', 'at', 'in', 'by', 
                'for', 'with', 'about', 'against', 
                'during', 'through', 'between', 'under', 
                'over', 'around', 'among', 'before', 'after'}

text = input().strip().lower()

words = [word for word in text.split() if word not in prepositions]

length_count = {}
normalized_word_groups = {}

for word in words:
    length = len(word)
    sorted_chars = ''.join(sorted(word))
    
    if length not in length_count:
        length_count[length] = 0
    length_count[length] += 1
    
    if sorted_chars not in normalized_word_groups:
        normalized_word_groups[sorted_chars] = 0
    normalized_word_groups[sorted_chars] += 1

length_count_filtered = {length: count for length, count in length_count.items() if count > 1}

similar_groups_count = sum(1 for count in normalized_word_groups.values() if count > 1)

if length_count_filtered:
    print(length_count_filtered)
else:
    print("{}")

print(similar_groups_count if similar_groups_count > 0 else 0)
