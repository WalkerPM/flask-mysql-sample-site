from flask import Flask, render_template
import pymysql


app = Flask(__name__)

@app.route('/')
def main_page():
    with con:
        cursor = con.cursor()
        cursor.execute('SELECT * from cars;')
        list = cursor.fetchall()
    return render_template('enumerate.html', listing = list )


if __name__ == "__main__":
    
 
    con = pymysql.connect(host='localhost', user='admin', password='P@ssw0rd', database='db2')
    app.run(port = 1488)