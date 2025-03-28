n = int(input())
heights_a = [int(x) for x in input().split()]
weights_class_a = [int(x) for x in input().split()]

m = int(input())
heights_b = [int(x) for x in input().split()]
weights_class_b = [int(x) for x in input().split()]


class_a_weights_mean = sum(weights_class_a) / n
class_b_weights_mean = sum(weights_class_b) / m

class_a_bmis = []
for i in range(n):
    
    this_bmi = weights_class_a[i] / (heights_a[i]/100)  ** 2
    class_a_bmis.append(this_bmi)

class_b_bmis = []
for i in range(m):

    this_bmi = weights_class_b[i] / (heights_b[i]/100) ** 2
    class_b_bmis.append(this_bmi)


bmi_class_a = round(sum(class_a_bmis)/n, 1)
bmi_class_b =  round(sum(class_b_bmis)/m, 1)
print(bmi_class_a)
print(bmi_class_b)

if bmi_class_a > bmi_class_b:
    print('B')

elif bmi_class_a == bmi_class_b:
    if class_a_weights_mean < class_b_weights_mean:
        print('A')

    elif class_a_weights_mean == class_b_weights_mean:
        print('Same')
    else:
        print('B')
else:
    print('A')