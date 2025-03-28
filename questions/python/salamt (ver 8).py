class Students:
    def __init__(self):
        self.class_a_bmis = []
        self.class_b_bmis = []

    def calss_1(self):
        numbers = int(input().strip())
        
        hights = []
        for qwe in map(int, input().split()):
            hights.append(qwe)
        
        wights = []
        for qwe in map(int, input().split()):
            wights.append(qwe)      

        return numbers, hights, wights

    def class_2(self):
        numbers = int(input().strip())

        hights = []
        for qwe in map(int, input().split()):
            hights.append(qwe)

        wights = []
        for qwe in map(int, input().split()):
            wights.append(qwe)

        return numbers, hights, wights
        

    def main(self):
        n, hights_c_1, weights_c_1 = self.calss_1()
        m, hights_c_2, weights_c_2 = self.class_2()

        #print(n, hights_c_1, weights_c_1, m, hights_c_2, weights_c_2)

        sum1 = 0
        for item in weights_c_1:
            sum1 += item
        sum2 = 0
        for item in weights_c_2:
            sum2 += item

        weights_mean_1 = sum1 / n
        weights_mean_2 = sum2 / m

        for i in range(n):
            mean = weights_c_1[i] / (hights_c_1[i]/100) ** 2
            self.class_a_bmis.append(mean)

        for i in range(m):
            mean =  weights_c_2[i] / (hights_c_2[i]/100) ** 2
            self.class_b_bmis.append(mean)

        bmi_c_1 = round(sum(self.class_a_bmis)/n, 1)
        bmi_c_2 =  round(sum(self.class_b_bmis)/m, 1)
        
        print(bmi_c_1)

        if bmi_c_1 > bmi_c_2: 
            print(bmi_c_2)
            print('B')
        elif bmi_c_1 == bmi_c_2:
            if weights_mean_1 < weights_mean_2:
                print(bmi_c_2)
                print('A')
            elif weights_mean_1 == weights_mean_2:
                print(bmi_c_2)
                print('Same')
            else:
                print(bmi_c_2)
                print('B')
        else:
            print(bmi_c_2)
            print('A')

bmi = Students()
bmi.main()