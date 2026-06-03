grades = {
    "Anna":   [85, 90, 78, 92],
    "Bob":    [70, 65, 80, 75],
    "Cathy":  [95, 88, 92, 100],
    "Diana":  [60, 70, 55, 65],
    "Eve":    [88, 95, 90, 92]
}

print("=== Student Grade Report ===")

top_student = ""
top_average = 0
worst_student = ""
worst_average = 100
class_total = 0

for name, student_grades in grades.items():
    avg = sum(student_grades) / len(student_grades)
    print(f"{name:<10} -> grades = {student_grades}   average ={avg:.2f}")
    
    if avg > top_average:
        top_average = avg
        top_student = name
        
    if avg < worst_average:
        worst_average = avg
        worst_student = name
        
    class_total = class_total + avg

class_average = class_total / len(grades) 
print(f"🏆 Top student: {top_student} with average of {top_average:.2f}")
print(f"📉 Needs improvement: {worst_student} with an average of {worst_average:.2f}")
print(f"📊 Class average: {class_average:.2f}")