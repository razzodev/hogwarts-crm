from flask import Flask, request, render_template, redirect
import time
import json
from data.student_data import students
from data.school_db import courses_db, skills_db
app = Flask(__name__)


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
    for course in courses_db:
        student[course] = request.form.get(course.replace(" ", ""))
    for skill in skills_db:
        student[skill] = request.form.get(skill.replace(" ", ""))
    students.append(student)
    print('add_student():', student)
    return redirect('http://127.0.0.1:5000/students')


@app.route('/student_profile/<id>')
def get_student_profile(id):
    for student in students:
        if student['id'] == id:
            return render_template('student_profile.html', student=student)


if __name__ == "__main__":
    app.run(debug=True)
