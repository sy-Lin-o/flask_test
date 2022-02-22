from flask import Flask
from flask import request,render_template
from flask_api import app
from flask import abort,redirect,url_for

@app.route('/login',methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
                return 'username/password pass'
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    #return 'Ps'
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(debug = True)