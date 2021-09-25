from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)
db = MySQL(app)

mydb = mysql.connector.connect(host="localhost", user="root",
                               password="Telefonica@2020", database="gpmio", port="3306")

mycursor = mydb.cursor()


def add(nome, senha, telefone):
    sql = "INSERT INTO dados (nome, senha, telefone) VALUES (%s, %s, %s)"
    val = (nome, senha, telefone)
    mycursor.execute(sql, val)
    mydb.commit()
    return 1


@app.route('/')
def index():
    return render_template("registrar.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route("/registro", methods=["POST", "GET"])
def Add():
    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        telefone = request.form["telefone"]
        add_new = add(nome, senha, telefone)
        return render_template('sucesso.html')

    else:
        print("error")
        return render_template('registrar.html')


if __name__ == '__main__':
    app.run(debug=True)
