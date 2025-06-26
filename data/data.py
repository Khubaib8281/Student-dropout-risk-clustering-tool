import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()
random.seed(42)
np.random.seed(42)

NUM_STUDENTS = 300

data = []

for i in range(1, NUM_STUDENTS + 1):
    student_id = i
    name = fake.name()
    age = random.randint(18, 25)
    gender = random.choice(['Male', 'Female'])


    quiz1 = np.clip(np.random.normal(7, 2), 0, 10)
    quiz2 = np.clip(np.random.normal(6, 2.5), 0, 10)
    quiz3 = np.clip(np.random.normal(5.5, 3), 0, 10)

    total_assignments = 5
    assignments_submitted = random.randint(0, total_assignments)

    midterm_marks = np.clip(np.random.normal(20, 10), 0, 30)
    final_marks = np.clip(np.random.normal(40, 15), 0, 50)

    previous_gpa = round(np.clip(np.random.normal(2.75, 0.75), 0, 4.0), 2)

    total_lectures = 12
    lectures_attended = random.randint(0, total_lectures)
    # attendance_ratio = round(lectures_attended / total_lectures, 2)

    total_lab_sessions = 6
    labs_attended = random.randint(0, total_lab_sessions)

    data.append([
        student_id, name, age, gender,
        round(quiz1, 1), round(quiz2, 1), round(quiz3, 1),
        total_assignments, assignments_submitted,
        round(midterm_marks, 1), round(final_marks, 1),
        previous_gpa,
        total_lectures, lectures_attended,
        total_lab_sessions, labs_attended
    ])

columns = [
    'student_id', 'name', 'age', 'gender',
    'quiz1_marks', 'quiz2_marks', 'quiz3_marks',
    'total_assignments', 'assignments_submitted',
    'midterm_marks', 'final_marks',
    'previous_gpa',
    'total_lectures', 'lectures_attended',
    'total_lab_sessions', 'labs_attended'
]

df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("student_dropout_behavior_dataset.csv", index=False)
print("Dataset saved as 'student_dropout_behavior_dataset.csv'")