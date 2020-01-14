from flask import Flask, request, render_template, redirect

students = []

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/students')
def students():
    return render_template('students.html', students=students)


@app.route('/new_student')
def new_student():
    return render_template('new_student.html')


@app.route('/new_student/add', methods=["POST"])
def add_student():
    print('students>>>>>>>>>', students)
    first_name = request.form.get('first_name')
    last_name = request.form.get('list_name')
    return str(students)


if __name__ == "__main__":
    app.run(debug=True)
