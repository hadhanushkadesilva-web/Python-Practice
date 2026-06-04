grades = {
    "Anna":   [85, 90, 78, 92],
    "Bob":    [70, 65, 80, 75],
    "Cathy":  [95, 88, 92, 100],
    "Diana":  [60, 70, 55, 65],
    "Eve":    [88, 95, 90, 92]
}

averages = {name: sum(scores) / len(scores) for name, scores in grades.items()}
for name, avg in averages.items():
    print(f"{name:<10} → grades = {grades[name]}   average = {avg:.2f}")
#best student, worst student, class average
best_student = max(averages, key=averages.get)
worst_student = min(averages, key=averages.get)
class_average = sum(averages.values()) / len(averages)

print(f"🏆 Top student: {best_student} with an average of {averages[best_student]:.2f}")
print(f"📉 Needs improvement: {worst_student} with an average of {averages[worst_student]:.2f}")
print(f"📊 Class average: {class_average:.2f}")