n = int(input())

storage = []
for _ in range(n):
    storage.append(input().split())


sorted_storage = sorted(storage, key=lambda x: (len(x), list(map(int, x))))
# Harf avale kelid ra baraye jabejayi set kardan
current_letter = "A"
last_line = sorted_storage[0]
# Chape matris moratab shode bar asase tedad va meghdar argham
#print(sorted_storage)
for line in sorted_storage:
    if line != last_line:
        current_letter = chr(ord(current_letter) + 1)

    # Peida kardan index khat baraye jabejayi harf
    #print(storage.index(line))
    storage[storage.index(line)] = current_letter
    last_line = line

text = ''
for stor in storage:
    text += stor

print(text)

