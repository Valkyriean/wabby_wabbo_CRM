# CRM by team Wabby Wabbo
University of Melbourne It Project

Guideline for system's configration:

Use 'npm run build' in frontend folder to compile the front end and drag the dist folder to flaskr/static for deployment.

Please set the global envirment variable of SECRET_KEY, DB_USERNAME, and DB_PASSWORD before running.

Run Server using:

gunicorn "flaskr:create_app()"
