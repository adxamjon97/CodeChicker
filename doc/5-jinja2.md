# jinja2 struktura

``` jinja2
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

``` py
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    return render_template("index.html",
        title = 'Home',
        user = user)
```

templates/base.html

``` j2
<html>
  <head>
    {% if title %}
    <title>{{title}} - microblog</title>
    {% else %}
    <title>microblog</title>
    {% endif %}
  </head>
  <body>
    <div>Microblog: <a href="/index">Home</a></div>
    <hr>
    {% block content %}{% endblock %}
  </body>
</html>
```

``` j2
{% extends "base.html" %}

{% block content %}
<h1>Hi, {{user.nickname}}!</h1>
{% for post in posts %}
<div><p>{{post.author.nickname}} says: <b>{{post.body}}</b></p></div>
{% endfor %}

{% endblock %}
```





















