from flask import Flask, render_template, session
import sqlite3


app = Flask(__name__)

db = sqlite3.connect('site.db')
cursor = db.cursor()
itens = cursor.execute( "SELECT * FROM user")
users = itens.fetchall()
print(users)

app.secret_key = '!@#users!@#'

@app.route('/')
def index():
   
    if 'usuario' in session:
        usuario = session['usuario']
        return usuario

if __name__ == '__main__':
    app.run(debug=True)