from flask import Flask, render_template as rt, make_response, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
	return rt("home.html")


@app.route("/projects")
def projects():
	return rt("projects.html")


@app.route("/blog")
def blog():
	return rt("blog.html")


@app.route('/reg', methods=['POST', 'GET'])
def reg():
	if request.method == 'POST':
		print("Nick:",  request.form['nick'])
		print("Email:", request.form['email'])
		print("Pass:",  request.form['pass'])
		print("Pass2:", request.form['pass2'])
		
	return rt('reg.html')

	
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['nick'],
                       request.form['pass']):
            return log_the_user_in(request.form['Nick'])
        else:
            error = 'username/password hato'
            
    return rt('auth.html', error=error)
    
    
"""
# ========= session =============
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
<form method="post">
	<fieldset>
		<legend>Kirish</legend>

		<input type="text"     name="nick" placeholder="Nick">
		<input type="password" name="pass" placeholder="Pass">
		<br>
		<input type="reset">
		<input type="submit">
	</fieldset>
</form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
    
"""


@app.errorhandler(404)
def not_found(error):
	return make_response(rt("404.html"), 404)	


if "__main__"==__name__:
	app.run(debug=True)
