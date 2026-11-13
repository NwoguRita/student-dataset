import csv

#Student records
students = [
    ["N-001", "Law", 400, 95, 95],
    ["N-002", "Economis", 200, 65, 71],
    ["N-003", "Philosophy", 100, 85, 82],
    ["N-004", "Biochemistry", 300, 72, 65],
    ["N-005", "Psychology", 400, 55, 45],
]

# Dataset column headings
headers = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score",
]

# Create the CSV file 
with open ("student_dataset.csv", "w",
newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(students)

    print("Student dataset craeted successfully")


