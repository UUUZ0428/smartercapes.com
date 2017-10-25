from flask import Flask, render_template
import json
app = Flask(__name__)

def load_json():
    with open('ranking.json') as f:
        ranking = json.load(f)
    with open('time.json') as f:
        time = json.load(f)
    with open('grade.json') as f:
        grade = json.load(f)
    return ranking, time, grade

ranking, time, grade = load_json()
print('Loaded json')

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/<dept>/<course>")
def welcome(dept, course):
    code = (dept + ' ' + course).upper()
    try:
        rank = ranking[code]
        hours = time[code]['time']
        time_color = time[code]['color']
        time_statement = time[code]['statement']
        
        expected_grade = grade[code]['expected_letter_grade']
        grade_color = grade[code]['color']
        grade_statement = grade[code]['statement']
    except KeyError:
        return render_template('nodata.html', code=code)
    
    return render_template("report.html", code=code, rank=rank, 
        hours=hours, time_color=time_color, time_statement=time_statement, 
        expected_grade=expected_grade, grade_color=grade_color, grade_statement=grade_statement)
    
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
