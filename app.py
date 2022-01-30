from flask import Flask, render_template, redirect, url_for, request
from sql import SQL
import json
import time


app = Flask(__name__)

sql = SQL()
sql.refresh_tables()


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


@app.route('/interview')
def interview():
    code = request.args.get("code")
    code = code.capitalize()

    if code.upper() in ['AJDU', 'LAYE', 'PXVF', 'MWBD']:
        return render_template('interview.html', code=code)
    else:
        return render_template('home.html')


@app.route('/query', methods=['GET', 'POST'])
def query():

    response = request.args.getlist('query')[0]

    response = sql.run_query(response)

    if response['error']:
        result = response['result']
        return(result), 201
    else:
        result = convert_to_json(response['result'])
        return(result)


@app.route('/refresh')
def refresh():
    sql.refresh_tables()

    return('successfulls refreshed')


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

    return(division_by_zero)


@app.errorhandler(404)
def page_not_found(e):

    return redirect(url_for('home'))


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
