from flask import Flask, request, render_template, url_for
from markupsafe import escape
import jinja2

def indexPage():
    return render_template('index.html')

app = Flask(__name__)

@app.route('/')
def rootPage():
    return indexPage()

@app.route('/user/<username>', methods=['GET','POST'])
def user_fun(username):
    if 'username' in request.form:
        return "Username: %s" % escape(username)
    else:
        return 'Sti Cazzi'

if __name__ == '__main__':
    app.run(debug=True)
