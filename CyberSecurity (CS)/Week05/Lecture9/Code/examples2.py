# Get list of students, calculate each student 
# average and get max average. 

def get_max_student_average(students):
    averages = []
    for student in students:
        total = 0
        for grade in students[student]:
            total += grade
        average = total/len(students[student])
        averages.append(average)
    
    max_average = max(averages)
    max_index = averages.index(max_average)

    student = list(students.keys())[max_index]

    print(f"Max Average\nStudent: {student}\nAverage: {max_average}")

students = {
    "James": [55, 76, 67, 68],
    "Jesicca": [60, 65, 70, 72],
    "Blake": [70, 75, 72, 71],
    "John": [65, 60, 77, 66],
    "Peter": [50, 50, 50, 50, 56, 67]
}
get_max_student_average(students)

print("Hello")