# CRM by team Wabby Wabbo
University of Melbourne It Project

Cheat sheet windows

Create virtual environment:
IF Windows:
py -3 -m venv venv
venv\Scripts\activate
IF Mac:
python3 -m venv venv
. venv/bin/activate
THEN:
pip install Flask
pip install wheel
pip install flask-mongoengine

Running:
IF Windows:
venv\Scripts\activate
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask run

IF Mac:
. venv/bin/activate
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

