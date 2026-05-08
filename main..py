from calculator import get_grade, get_average, get_highest, get_lowest

students = [
    {"name": "Alice", "scores": [88, 92, 79]},
    {"name": "Bob", "scores": [70, 65, 80]},
    {"name": "Carlos", "scores": [95, 98, 100]},
    {"name": "Diana", "scores": [55, 60, 58]},
    {"name": "Eve", "scores": [72, 68, 75]},
    {"name": "Ian", "scores": [92, 93, 97]},
]

print("=" * 55)
print(f"{'NAME':<10} {'AVERAGE':>8} {'GRADE':>6} {'HIGHEST':>8} {'LOWEST':>7}")
print("=" * 55)

for student in students:
    avg = get_average(student["scores"])
    grade = get_grade(avg)
    highest = get_highest(student["scores"])
    lowest = get_lowest(student["scores"])
    print(f"{student['name']:<10} {avg:>8.1f} {grade:>6} {highest:>8} {lowest:>7}")

print("=" * 55)