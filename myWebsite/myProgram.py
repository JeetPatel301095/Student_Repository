from flask import Flask, render_template
# from .Student_Repository.Student_Repository_Jeet_Divyangbhai_Patel import University
import sqlite3


app: Flask = Flask(__name__)

@app.route('/Hello')
def hello() ->str:
    return "Hello World! This is Flask!"

@app.route('/print_students')
def template_demo() ->str:
    db_path = "C:/Users/Jeet/Jeet/SW-810/Student_Repository/810_startup.db"
    db: sqlite3.Connection = sqlite3.connect(db_path)
    studict: List[Dict[str,str]] = list()
    query:str = "select a.Name,a.CWID,b.Course,b.Grade,b.Name from students a join (select Name,Course,Grade,StudentCWID from instructors c join grades d on c.CWID = d.InstructorCWID) b on a.CWID = b.StudentCWID;"
    for row in db.execute(query):
        # print(row)
        dic: Dict[str,str] = {
            'name': row[0],
            'cwid': row[1],
            'course': row[2],
            'grade': row[3],
            'inst': row[4]
        }
        studict.append(dic)
    return render_template('parameters.html',table_title ="Students Grade Table", students= studict)
    # return render_template('parameters.html',my_header = "My Stevens Repository", my_param= "My Custom Parameter")

app.run(debug=True)