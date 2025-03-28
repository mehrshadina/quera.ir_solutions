text1 = input()
text1_copy = text1
text2 = input()

first_words = ''.join(list(filter(('-').__ne__, text1))).split('_')
seccond_words = ''.join(list(filter(('_').__ne__, text1_copy))).split('-')

#print(first_words)
#print(seccond_words)


for word in first_words:
   if len(word) > 2:
      text2 = text2.replace(word, '')

for word in seccond_words:
   if len(word) > 2:
      text2 = text2.replace(word, '')

print(text2)