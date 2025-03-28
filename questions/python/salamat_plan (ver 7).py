def calculate_bmi(height, weight):
    return weight / ((height / 100) ** 2)

def average_bmi(heights, weights):
    bmis = [calculate_bmi(h, w) for h, w in zip(heights, weights)]
    return round(sum(bmis) / len(bmis), 1)

def average_weight(weights):
    return round(sum(weights) / len(weights), 1)

def compare_classes(heights_a, weights_a, heights_b, weights_b):
    avg_bmi_a = average_bmi(heights_a, weights_a)
    avg_bmi_b = average_bmi(heights_b, weights_b)
    
    if avg_bmi_a < avg_bmi_b:
        return "A"
    elif avg_bmi_b < avg_bmi_a:
        return "B"
    else:
        avg_weight_a = average_weight(weights_a)
        avg_weight_b = average_weight(weights_b)
        
        if avg_weight_a < avg_weight_b:
            return "A"
        elif avg_weight_b < avg_weight_a:
            return "B"
        else:
            return "Same"

num_students_a = int(input())
heights_a = list(map(int, input().split()))
weights_a = list(map(int, input().split()))

num_students_b = int(input())
heights_b = list(map(int, input().split()))
weights_b = list(map(int, input().split()))

print(average_bmi(heights_a, weights_a))
print(average_bmi(heights_b, weights_b))
print(compare_classes(heights_a, weights_a, heights_b, weights_b))
