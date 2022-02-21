from flask import Flask, render_template, redirect, url_for, request, flash
from sql import SQL
import json
import time
import sqlparse
import os
import json


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def convert_to_json(results):
    master = {}
    counter = 1

    for row in results:
        print(row)
        master[counter] = row
        counter += 1

    print(master)
    return(master)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/<sql_type>/interview')
def interview(sql_type):

    sql = SQL(sql_type)
    questions = sql.get_questions()

    for question in questions:
        print(question)
        questions[question]['answer'] = sql.run_query(
            questions[question]['query'])

    code = request.args.get("code")
    code = code.capitalize()

    try:
        env_list = json.loads(os.environ['ALLOWED_USERS'])
        if code in env_list:
            allowed = True
        else:
            allowed = False
    except KeyError:
        allowed = True

    if not allowed:
        flash('Invalid code.')
        return redirect('/')

    db_creation_script = sqlparse.format(
        sql.get_table_script(), reindent=False, keyword_case='upper')

    print(db_creation_script)

    return render_template('interview.html', code=code, questions=questions, sql_type=sql_type, tables=sql.get_table_info(), creation_script=db_creation_script)


@app.route('/query', methods=['GET', 'POST'])
def query():

    sql = SQL('investments')

    response = request.args.getlist('query')[0]

    response = sql.run_query(response)
    print('response')
    print(response)

    if response['error']:
        result = response['result']
        return(result), 201
    else:
        result = convert_to_json(response['result'])
        return(result)


@app.route('/questions_info', methods=['GET', 'POST'])
def questions_info():

    sql = SQL('investments')
    questions = sql.get_questions()

    for question in questions:
        # del questions[question]['query']
        questions[question]['answer'] = sql.run_query(
            questions[question]['query'])

    return(questions)


@app.route('/get_schema', methods=['GET', 'POST'])
def get_schema():

    sql = SQL('investments')
    questions = sql.get_questions()

    for question in questions:
        del questions[question]['query']
        questions[question]['answer'] = sql.run_query(
            questions[question]['query'])

    return(questions)


@app.route('/<sql_type>/refresh')
def refresh(sql_type):
    SQL(sql_type)

    return('successfulls refreshed')


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

    return(division_by_zero)


# @app.errorhandler(404)
# def page_not_found(e):

#     return redirect(url_for('home'))


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

    # print(env_list[0])
