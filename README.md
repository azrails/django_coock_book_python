# cook_book

docker-compose build 
docker-compose up

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
