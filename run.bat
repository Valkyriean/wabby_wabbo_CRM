@REM call python -m venv venv
@REM call venv\Scripts\activate.bat
REM call python -m pip install --upgrade pip
REM call pip install -r requirements.txt
REM call npm install
REM use flask dbupdate for dropping existing database and rolling all new tabels
REM call flask dbcreate
@REM call npm run dev
@REM call flask run

call venv\Scripts\activate
call set FLASK_APP=flaskr
call set FLASK_ENV=development
call flask run