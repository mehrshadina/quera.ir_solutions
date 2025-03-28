import pandas as pd

def calculate_bmi(row):
    return row['weight'] / ((row['height'] / 100) ** 2)

def compare_classes(df_a, df_b):
    avg_bmi_a = round(df_a['bmi'].mean(), 1)
    avg_bmi_b = round(df_b['bmi'].mean(), 1)
    
    if avg_bmi_a < avg_bmi_b:
        return "A"
    elif avg_bmi_b < avg_bmi_a:
        return "B"
    else:
        avg_weight_a = round(df_a['weight'].mean(), 1)
        avg_weight_b = round(df_b['weight'].mean(), 1)
        
        if avg_weight_a < avg_weight_b:
            return "A"
        elif avg_weight_b < avg_weight_a:
            return "B"
        else:
            return "Same"

# Input
num_students_a = int(input())
heights_a = list(map(int, input().split()))
weights_a = list(map(int, input().split()))

num_students_b = int(input())
heights_b = list(map(int, input().split()))
weights_b = list(map(int, input().split()))

df_a = pd.DataFrame({'height': heights_a, 'weight': weights_a})
df_b = pd.DataFrame({'height': heights_b, 'weight': weights_b})

df_a['bmi'] = df_a.apply(calculate_bmi, axis=1)
df_b['bmi'] = df_b.apply(calculate_bmi, axis=1)

result = compare_classes(df_a, df_b)
print(round(df_a['bmi'].mean(), 1))
print(round(df_b['bmi'].mean(), 1))
print(result)
