Official doc: https://flask.palletsprojects.com/en/2.0.x/quickstart/

# start

``` py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def route():
	return "hello world"
```


# html viewer

``` py
from markupsafe import escape

@app.route("/<name>")
def hello(name):
	return f"Hello, {escape(name)}!"
```


# marshrutizatsya

``` py
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```


# o'zgaruvchilar tartibi

``` py
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

var    | discription                           |
-------|---------------------------------------|
string | текст без косой черты                 |
int    | целые числа                           |
float  | значения с плавающей запятой          |
path   | string но также принимает косые черты |
uuid   | строки UUID                           |


# unikalniy addres

``` py
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```


# url_for


``` py
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

javob

``` console
/
/login
/login?next=/
/user/John%20Doe
```


# http methods

``` py
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```


# static files

create /static

``` py
url_for('static', filename='style.css')
```

# shablon

``` py
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

modulniy struktura

``` 
/application.py
/templates
    /hello.html
```

paketli struktura

```
/application
    /__init__.py
    /templates
        /hello.html
```






















