from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)  # spravi z tohto suboru web aplikaciu


db = mysql.connector.connect(host='localhost', port='3308', database='glbank', user='root', password='')


@app.route("/")  # pripajanie na web
def index():  # whoami bude default
    return render_template("index.html", )  # uz mam konkretnu stranku svoju, ak prijma parameter tak /?name=Mim


@app.route("/register", methods=["POST"])
def register():
    login = request.form.get("name")
    password = request.form.get("pass")
    if not login or not password:
        return "fail"
    cur = db.cursor()
    query = "SELECT * FROM Employee inner join loginemp on Employee.id=loginemp.ide where login = %s and password = %s"
    cur.execute(query, (login, password))
    result = cur.fetchone()
    print(result)
    return render_template("succesful.html")


if __name__ == "__main__":
    app.run()
