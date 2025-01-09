from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'

# @app.route('/')
# def index():
#     con = sqlite3.connect(DATABASE)
#     db_books = con.execute('SELECT * FROM books').fetchall()
#     con.close()
#     books = [
#         # {'title':'縺ｯ繧峨⊆縺薙≠縺翫�縺�',
#         #  'price':1200,
#         #  'arrival_day':'2020蟷ｴ7譛�12譌･'},
        
#         # {'title':'縺舌ｊ縺ｨ縺舌ｉ',
#         #  'price':990,
#         #  'arrival_day':'2020蟷ｴ7譛�13譌･'},
#     ]
#     for row in db_books:
#         books.append({'title': row[0], 'price': row[1], 'arrival_day': row[2]})

#     return render_template(
#         'index.html',
#         books=books
#     )


# @app.route('/form')
# def form():
#     return render_template(
#         'form.html'
#     )

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/question1')
def question1():
    return render_template('question1.html')
@app.route('/question2')
def question2():
    return render_template('question2.html')
@app.route('/result')
def result():
    return render_template('result.html')



if __name__ == '__main__':
    app.run(debug=True)
