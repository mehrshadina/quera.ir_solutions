class Students:
    def __init__(self):
        self.class_a_bmis = []
        self.class_b_bmis = []

    def get_information(self):
        n = int(input().strip())
        
        h = []
        for qwe in map(int, input().split()):
            h.append(qwe)
        
        w = []
        for qwe in map(int, input().split()):
            w.append(qwe)            

        m = int(input().strip())

        h1 = []
        for qwe in map(int, input().split()):
            h1.append(qwe)

        w2 = []
        for qwe in map(int, input().split()):
            w2.append(qwe)

        return n, h, w, m, h1, w2

    def main(self):
        n, hights_class_a, weights_class_a, m, hights_class_b, weights_class_b = self.get_information()
        class_a_weights_mean = sum(weights_class_a) / n
        class_b_weights_mean = sum(weights_class_b) / m

        for i in range(n):
            a = weights_class_a[i]
            b = hights_class_a[i]/100
            c = a / b ** 2
            self.class_a_bmis.append(c)

        for i in range(m):
            a = weights_class_b[i]
            b = hights_class_b[i]/100
            c =  a / b ** 2
            self.class_b_bmis.append(c)

        bmi_class_first = round(sum(self.class_a_bmis)/n, 1)
        bmi_class_second =  round(sum(self.class_b_bmis)/m, 1)
        
        if bmi_class_first > bmi_class_second:
            print(bmi_class_first)
            print(bmi_class_second)
            print('B')
        elif bmi_class_first == bmi_class_second:
            if class_a_weights_mean < class_b_weights_mean:
                print(bmi_class_first)
                print(bmi_class_second)
                print('A')
            elif class_a_weights_mean == class_b_weights_mean:
                print(bmi_class_first)
                print(bmi_class_second)
                print('Same')
            else:
                print(bmi_class_first)
                print(bmi_class_second)
                print('B')
        else:
            print(bmi_class_first)
            print(bmi_class_second)
            print('A')

bmi_cal = Students()
#bmi_cal.get_information()
bmi_cal.main()