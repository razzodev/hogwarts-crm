from flask import Flask, request, render_template, redirect, jsonify
import time
import json
import pickle
from data.student_data import students
from data.school_db import courses_db, skills_db
app = Flask(__name__)

with open('./data/students_db.json') as file:
    students = json.load(file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/students')
def getstudents():
    return render_template('students.html', students=students)


@app.route('/new_student')
def new_student():
    course_list = []
    skill_list = []
    return render_template('new_student.html', courses=courses_db, skills=skills_db)


@app.route('/new_student/add', methods=["POST"])
def add_student():
    student = {}
    student['first_name'] = request.form.get('first_name')
    student['last_name'] = request.form.get('last_name')
    student['time_created'] = time.time()
    student['time_updated'] = time.time()
    student['id'] = f"ID:{student['first_name']}{int(time.time())}"
    student['courses'] = []
    student['skills'] = {}
    for course in courses_db:
        # print('>>>>>>>>>>>>>>>', request.form.get(course.replace(" ", "")))
        if request.form.get(course.replace(" ", "")):
            student['courses'].append(course)
    for skill in skills_db:
        if request.form.get(skill.replace(" ", "")):
            student['skills'][skill] = int(
                request.form.get(skill.replace(" ", "")))
    students.append(student)
    print('add_student():', student)
    render_template('students.html', student=student)
    return redirect('/students')


@app.route('/student_profile/<id>')
def get_student_profile(id):
    for student in students:
        if student['id'] == id:
            return render_template('student_profile.html', student=student, courses=student['courses'])


@app.route('/student_profile/delete/<id>')
def del_student_profile(id):
    students[:] = [student for student in students if student['id'] != id]
    return redirect('/students')


@app.route('/students/save_DB')
def save_students_to_db():
    with open('./data/students_db.json', 'w') as file:
        json.dump(students, file)
    return str('check students_db.json')


if __name__ == "__main__":
    app.run(debug=True)
