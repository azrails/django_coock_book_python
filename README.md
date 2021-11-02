# coocking book
## Summary: The project includes a cookbook app, 
frontend: bootstrap standard templates, html, css, 
backend: django, postgres, 
server: docker cluster.
![Alt text](./13.png)
#### :warning: Note: add_recipe and add_ingridient in betta.

### Note:
:warning: To install you need installed before: docker, docker compose

### :star: Instalation steps:
1) clone project and change to directory.
#### Create a .env.dev file and write this config into it
#### (if necessary, you can replace the necessary parameters here and in docker-compose.yaml):
DEBUG=1<br>
SECRET_KEY=foo<br>
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]<br>
POSTGRES_ENGINE=django.db.backends.postgresql<br>
POSTGRES_DB=django_cook<br>
POSTGRES_USER=django_user<br>
POSTGRES_PASSWORD=django_password<br>
POSTGRES_HOST=db<br>
POSTGRES_PORT=5432<br>
#### To build and run project.
2) docker-compose up --build
Create tables on your database.
3) sudo docker-compose exec web python manage.py makemigrations
4) sudo docker-compose exec web python manage.py migrate
5) sudo docker-compose exec web python manage.py makemigrations book
6) sudo docker-compose exec web python manage.py migrate book
7) sudo docker-compose exec web python manage.py loaddata fixtures.json
8) sudo docker-compose exec web python manage.py createsuperuser
### :warning:Note: 
if you see a similar picture after all steps or don't see ingridient filter:
![Alt text](./12.png)
Stop the project runing(ctrl-c) and rerun step 2
until you see something like this.
![Alt text](./11.png)
