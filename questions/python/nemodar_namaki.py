import numpy as np

def calculate_curve_length(a, b, c, d, x_min=-10, x_max=10, dx=0.001):
    x_values = np.arange(x_min, x_max, dx)
    y_values = a * x_values**3 + b * x_values**2 + c * x_values + d
    dy_dx = 3 * a * x_values**2 + 2 * b * x_values + c
    lengths = np.sqrt(1 + dy_dx**2) * dx
    total_length = np.sum(lengths)
    return total_length

def main(grades_str):
    grades = list(map(float, grades_str.split()))
    n = len(grades)
    
    mean = np.mean(grades)
    std_dev = np.std(grades)
    
    # Coefficients for cubic curve: f(x) = ax^3 + bx^2 + cx + d
    a = 0  # Assuming no cubic term for simplicity
    b = 0  # Assuming no quadratic term for simplicity
    c = std_dev
    d = mean
    
    total_length = calculate_curve_length(a, b, c, d)
    length_per_student = total_length / n
    
    # Assign lengths to students based on their grades
    sorted_grades = sorted(grades)
    assigned_lengths = [length_per_student * (i + 1) for i in range(n)]
    
    # Calculate new grades based on the average y of the first and last points
    new_grades = []
    for i in range(n):
        x_start = -10 + assigned_lengths[i]
        x_end = -10 + assigned_lengths[i] + length_per_student
        y_start = a * x_start**3 + b * x_start**2 + c * x_start + d
        y_end = a * x_end**3 + b * x_end**2 + c * x_end + d
        avg_y = (y_start + y_end) / 2
        new_grades.append(avg_y)
    
    # Adjust grades
    max_grade = max(new_grades)
    ratio = max_grade / 10
    adjusted_grades = [grade / ratio for grade in new_grades]
    
    mean_adjusted = np.mean(adjusted_grades)
    constant = 17 - mean_adjusted
    final_grades = [grade + constant for grade in adjusted_grades]
    
    # Repeat the adjustment
    max_grade_final = max(final_grades)
    ratio_final = max_grade_final / 10
    final_adjusted_grades = [grade / ratio_final for grade in final_grades]
    
    mean_final_adjusted = np.mean(final_adjusted_grades)
    constant_final = 17 - mean_final_adjusted
    final_grades_second = [grade + constant_final for grade in final_adjusted_grades]
    
    # Set the last grade to f(x=10)
    last_grade = a * 10**3 + b * 10**2 + c * 10 + d
    final_grades_second[-1] = last_grade
    
    # Round to one decimal place
    final_grades_rounded = [round(grade, 1) for grade in final_grades_second]
    
    return final_grades_rounded

# Example usage
grades_str = "13 18 15 11 19 14 10 17 16 20 15 12 17 18 11 19"
result = main(grades_str)
print(result)