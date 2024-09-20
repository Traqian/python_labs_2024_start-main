import json

# 打开并读取JSON文件
with open('D:\\Download\\python_labs_2024_start-main\\python_labs_2024_start-main\\students.json', 'r') as f:
    data = json.load(f)

students = data['students']

# data现在是一个字典，可以像处理普通字典一样处理它
for student in data['students']:
    print(f"Student ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")