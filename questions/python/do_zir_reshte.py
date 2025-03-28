text = input()

def find(phrase, obj):
    len_phrase = len(phrase)
    len_obj = len(obj)

    #print(len_phrase-len_obj)
    for i in range(len_phrase-len_obj+1):
        #print(i)
        if obj in phrase[i:i+len_obj]:
            return i
    else:
        return 0

#print(find(text, 'AB'))
#print(find(text, 'BA'))
if ((find(text, 'AB') - find(text, 'BA')) ** 2) > 2:
    print('YES')
else:
    print('NO')