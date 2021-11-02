# coocking book
## Summary: The project includes a cookbook app, 
frontend: bootstrap standard templates, html, css, 
backend: django, postgres, 
server: docker cluster.

### Note:
:warning: To install you need installed before: docker, docker compose

1) docker-compose up --build
2) sudo docker-compose exec web python manage.py makemigrations
3) sudo docker-compose exec web python manage.py migrate
4) sudo docker-compose exec web python manage.py makemigrations book
5) sudo docker-compose exec web python manage.py createsuperuser


.env.dev:
DEBUG=1
SECRET_KEY=foo
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_DB=django_cook
POSTGRES_USER=django_user
POSTGRES_PASSWORD=django_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
