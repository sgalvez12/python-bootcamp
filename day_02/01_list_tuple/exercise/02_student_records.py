student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)

for student, score in zip(student_names, student_scores):
    print(student, score)
# TODO: Print the student scores and names in the following format
""" 
    Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
"""
for student, score in zip(student_names, student_scores):
print(f"Student: {student} scored {score} in the exam")

#highest score
highest_scorer = None
highest_score = None



