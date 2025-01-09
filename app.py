from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# �f�[�^�x�[�X���玿����擾����֐�
def get_questions():
    # �f�[�^�x�[�X�ɐڑ�
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # ��������ׂĎ擾
    cursor.execute('SELECT * FROM questions')
    questions = cursor.fetchall()

    # �ڑ������
    conn.close()

    # �擾�����f�[�^��Ԃ�
    return questions

@app.route('/')
def index():
    # �f�[�^�x�[�X���玿����擾
    questions = get_questions()

    # �e���v���[�g�ɓn���ĕ\��
    return render_template('index.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)