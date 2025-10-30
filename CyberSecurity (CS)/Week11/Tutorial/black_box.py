"""Module Docstring"""
def assign_grade(score):
    """Function DOc"""
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return "Invalid Score"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

def process_grades(scores):
    """Function DOc"""
    return [assign_grade(score) for score in scores]



# [95, 85, 75, 65, 55]  --> ["A", "B", "C", "D", "F"]
print(process_grades([95, 85, 75, 65, 55]))

# [100, 90, 80, 70, 60, 50] --> ["A", "A", "B", "C", "D", "F"]
print(process_grades([100, 90, 80, 70, 60, 50]))

# [110, -5] --> ["Invalid Score", "Invalid Score"]
print(process_grades([110, -5]))

print(process_grades(["A", 85, None, 70.1]))
