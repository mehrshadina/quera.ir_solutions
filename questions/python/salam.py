class hospital:
    def __init__(self):
        self.class_a_bmis = []
        self.class_a_weights_mean = 0
        self.class_b_bmis = []
        self.class_b_weights_mean = 0
        self.na = 0
        self.nb = 0


    def main(self):
        self.na = int(input())
        ha = list(map(int, input().split()))
        wa = list(map(int, input().split()))

        self.nb = int(input())
        hb = list(map(int, input().split()))
        wb = list(map(int, input().split()))

        self.class_a_weights_mean = sum(wa) / self.na
        self.class_b_weights_mean= sum(wb) / self.nb

        for i in range(self.na):
            this_bmi = wa[i] / (ha[i]/100)  ** 2
            self.class_a_bmis.append(this_bmi)

        for i in range(self.nb):
            this_bmi = wb[i] / (hb[i]/100) ** 2
            self.class_b_bmis.append(this_bmi)


    def result(self):
        bca = round(sum(self.class_a_bmis)/self.na, 1)
        bcb =  round(sum(self.class_b_bmis)/self.nb, 1)
        print(bca)
        print(bcb)

        if bca > bcb:
            print('B')
        elif bca == bcb:
            if self.class_a_weights_mean < self.class_b_weights_mean:
                print('A')
            elif self.class_a_weights_mean == self.class_b_weights_mean:
                print('Same')
            else:
                print('B')
        else:
            print('A')

bmi = hospital()
bmi.main()
bmi.result()