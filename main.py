from flask import Flask, render_template
import pymysql


app = Flask(__name__)

def get_all():
    list = []
    con = pymysql.connect(host='localhost', user='admin', password='P@ssw0rd', database='db2')
    with con:
        cursor = con.cursor()
        cursor.execute('SELECT * from cars;')
        list = cursor.fetchall()
    return list

@app.route('/fetch-all')
def fetchall_page():
    return render_template('enumerate.html', listing = get_all() )
@app.route("/")
def main_page():
    return render_template('main-page.html')


if __name__ == "__main__":
    app.run(port = 1480)