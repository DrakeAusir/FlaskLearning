from flask import Flask, request, render_template, url_for, redirect
from markupsafe import escape
from config import Config
import jinja2

### Creazione e settings dell'oggetto Flask App
app = Flask(__name__)
app.config.from_object(Config)

#### Dichiarazioni e Definizioni di funzioni
def indexPage():
	return render_template('index.html')

### Funzione di TEST
def testFunction(var):
	return var

### Definizione delle Routes
@app.route('/')
def rootPage():
    return indexPage()

@app.route('/user/', methods=['GET',' POST'])
def userPage():
	username = request.args.get('username')
	return render_template('user.html', name=username)

	### definizione 404
@app.errorhandler(404)
def page_not_found(e):
	return 'WTF \n {}'.format(e)

### Inizio Main
if __name__ == '__main__':
    app.run(debug=True)
