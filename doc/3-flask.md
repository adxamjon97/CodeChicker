# install flask
pip install Flask

# create py file
touch start.py

# bog'lash
export FLASK_APP=start

# ishga tushirish
flask run

# tashqi setga ko'rinishi uchun
flask run --host=0.0.0.0

# dasturchi holati
export FLASK_ENV=development
