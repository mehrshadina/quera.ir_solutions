def apply_operations(word):
    i = 0
    while i < len(word):
        if word[i] == 'x':
            if i + 1 < len(word) and word[i+1] == 'x':
                word = word[:i] + word[i+1:]
            else:
                word = word[i+1:] + word[:i][::-1]
                i = 0
                continue
        
        elif word[i] == 'w':
            if i + 1 < len(word):
                if word[i+1] == 'w':
                    word = word[:i] + word[i+1:]
                elif word[i+1] != 'w':
                    word = word[:i] + word[-1] + word[i+2:-1] + word[i+1]
            else :
                word = word[:-1]
            
        i += 1
    return word
               
sentence = input().strip().split()

for i in range(len(sentence)):
    sentence[i] = apply_operations(sentence[i])

print(' '.join(sentence))
