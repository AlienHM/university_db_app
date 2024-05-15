from flask import Flask, request, render_template, redirect, url_for
import redis
import json

app = Flask(__name__)
db = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def reset_db():
    db.flushdb()
    majors = ['Kompüter Elmləri', 'Biologiya', 'Fizika', 'Tarix', 'Mühəndislik', 'Riyaziyyat']
    db.set('majors', json.dumps(majors))

@app.route('/', methods=['GET', 'POST'])
def index():
    query = request.form.get('query', '').lower()
    filter_role = request.form.get('filter_role', 'all')
    student_keys = db.scan_iter("student:*")
    teacher_keys = db.scan_iter("teacher:*")
    students = [json.loads(db.get(key)) for key in student_keys]
    teachers = [json.loads(db.get(key)) for key in teacher_keys]

    # Filter data based on query and role
    if query:
        if filter_role == 'student' or filter_role == 'all':
            students = [s for s in students if query in s['name'].lower() or query in s['major'].lower()]
        if filter_role == 'teacher' or filter_role == 'all':
            teachers = [t for t in teachers if query in t['name'].lower() or query in t['major'].lower()]

    majors = json.loads(db.get('majors'))
    return render_template('index.html', students=students, teachers=teachers, majors=majors, query=query, filter_role=filter_role)

@app.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        name = request.form['name']
        major = request.form['major']
        year = request.form['year']
        role = request.form['role']
        next_id = db.incr(f'{role}_id')
        data = {'id': next_id, 'name': name, 'major': major, 'year': year}
        db.set(f'{role}:{next_id}', json.dumps(data))
        return redirect(url_for('index'))
    majors = json.loads(db.get('majors'))
    return render_template('add_data.html', majors=majors)

@app.route('/reset', methods=['POST'])
def reset():
    reset_db()
    return redirect(url_for('index'))

if __name__ == '__main__':
    reset_db()
    app.run(debug=True)
