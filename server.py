from flask import Flask, request, render_template, redirect
import time
from data.data import students

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/students')
def getstudents():
    return render_template('students.html', students=students)


@app.route('/new_student')
def new_student():
    return render_template('new_student.html')


@app.route('/new_student/add', methods=["POST"])
def add_student():
    student = {}
    student['first_name'] = request.form.get('first_name')
    student['last_name'] = request.form.get('last_name')
    student['time_created'] = time.time()
    student['time_updated'] = time.time()
    students.append(student)
    print('add_student():', students)
    return redirect('http://127.0.0.1:5000/students')


if __name__ == "__main__":
    app.run(debug=True)
