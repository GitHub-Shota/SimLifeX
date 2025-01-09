from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# データベースから質問を取得する関数
def get_questions():
    # データベースに接続
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # 質問をすべて取得
    cursor.execute('SELECT * FROM questions')
    questions = cursor.fetchall()

    # 接続を閉じる
    conn.close()

    # 取得したデータを返す
    return questions

@app.route('/')
def index():
    # データベースから質問を取得
    questions = get_questions()

    # テンプレートに渡して表示
    return render_template('index.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)