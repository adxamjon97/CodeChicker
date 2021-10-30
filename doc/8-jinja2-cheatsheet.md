# jinja2 cheatsheet

{% extends "base.html" %} {% endblock %} - import
{% block content %} {% endfor %} - put
{{ user.name }} - var render_template('path_to_file', user={'name':'adxamjon'})
{% if False %} {% elif True %} {% else %} {% endif %} - if sharti
{% set lst=[0,1,2,3] %}

{% for user in users %} <li>{{ user }}</li> {% endfor %} - for sikli 
