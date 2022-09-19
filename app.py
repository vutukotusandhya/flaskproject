from flask import Flask, render_template, request, redirect
import MySQLdb
app = Flask(__name__)

# Configure db

conn=MySQLdb.connect(
        host='localhost',
        user='root',
        password = 'Sandhya@24',
        db='employee',
        )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        emp_id = userDetails['emp_id']
        emp_name = userDetails['emp_name']
        emp_dept = userDetails['emp_dept']
        cur = conn.cursor()
        cur.execute("INSERT INTO emp(emp_id, emp_name, emp_dept) VALUES(%s, %s, %s)",(emp_id, emp_name, emp_dept))
        conn.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/countofemp')
def countofemp():
    cur = conn.cursor()
    resultValue = cur.execute("SELECT COUNT(emp_id) FROM emp  WHERE emp_dept='BDA'")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)


@app.route('/emp_name')
def emp_name():
    cur = conn.cursor()
    resultValue = cur.execute(" SELECT emp_name FROM emp WHERE emp_name LIKE 'S%' ")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")