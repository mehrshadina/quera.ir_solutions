w1, a1 = input().split()
w2, a2 = input().split()
w3, a3 = input().split()
w4, a4 = input().split()
w5, a5 = input().split()

a1, a2, a3, a4, a5 = int(a1), int(a2), int(a3), int(a4), int(a5)

data = [(w1, a1), (w2, a2), (w3, a3), (w4, a4), (w5, a5)]

data = sorted(data, key=lambda x: x[1], reverse=True)

(w1, a1), (w2, a2), (w3, a3), (w4, a4), (w5, a5) = data

print("First :", w1)
print("Second :", w2)
print("Third :", w3)
print("Fourth :", w4)
print("Fifth :", w5)
