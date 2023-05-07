from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import openai
import sqlite3
import json

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS prompts (prompt TEXT, response TEXT)')

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            load_dotenv()
            openai.api_key = os.getenv("OPENAI_API_KEY")
            processed_text = text.upper()
            submit_pressed = True
            models = openai.Model.list()
            model_engine = "davinci"
            response = openai.Completion.create(
                prompt=processed_text,
                max_tokens=50,
                n=1,
                stop=None,
                temperature=0.5,
                frequency_penalty=0,
                presence_penalty=0,
                model="text-davinci-002",
            )
            output_text = str(response)
            json_obj = json.loads(output_text)
            output_text = json_obj['choices'][0]['text']
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO prompts (prompt, response) VALUES (?, ?)", (text, str(output_text)))
                con.commit()
            return render_template('index.html', processed_text=str(output_text), models=models,
                                   submit_pressed=submit_pressed)
        else:
            return 'Error: Form data is incomplete.'
    else:
        return render_template('index.html')


# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form.get('text')
#     if text:
#         load_dotenv()
#         openai.api_key = os.getenv("OPENAI_API_KEY")
#         processed_text = text.upper()
#         submit_pressed = True
#         output_text = openai.Completion.create(
#                       model="text-davinci-002",
#                       prompt=processed_text,
#                       max_tokens=7,
#                       temperature=0
#                     )
#         return render_template('index.html', processed_text=output_text, submit_pressed=submit_pressed)
#     else:
#         return 'Error: Form data is incomplete.'

@app.route('/prompts', methods=['GET'])
def prompts_page():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM prompts")
    data = cur.fetchall()
    return render_template('prompts_page.html', data=data)
