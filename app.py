from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (list of dictionaries)
students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        progress = request.form['progress']

        student = {
            'name': name,
            'subject': subject,
            'progress': progress
        }

        students.append(student)
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/view/<int:id>')
def view(id):
    student = students[id]
    return render_template('view.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)