web: gunicorn agileProject.wsgi
web: python agileProject/manage.py collectstatic --noinput ; gunicorn --bind 0.0.0.0:$PORT agileProject.wsgi:application
