web: gunicorn agileProject.wsgi
web: python my_django_app/manage.py collectstatic --noinput ; gunicorn --bind 0.0.0.0:$PORT agileProject.wsgi:application
