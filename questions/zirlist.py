input_str = input()
list1_str, list2_str = input_str.split('] [')

if list2_str[:-1].strip().replace(',', '').replace(' ', '') in list1_str[1:].strip().replace(',', '').replace(' ', ''):
    print("YES")
else:
    print("NO")