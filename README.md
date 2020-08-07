# Django and PostgreSQL on Docker :rocket:
Use this project to start a Djando Project with PosgreSQL.

Clone with:
```
git clone https://github.com/iraidamercedes/django_base_project.git
```
Create a .env.dev file in the root folder and set the values for the following parameters:

```
DEBUG=1
SECRET_KEY=
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=db
SQL_PORT=5432
```

Buld the image with:
```
docker-compose build
```

Run the cointainer:
```
docker-compose up -d
```

If you want to create another repository based o this project, you can change the remote origin with the following command:

```
git remote set-url origin <url>
```

To run the migrations use the following onstruction:
```
docker-compose exec web python manage.py migrate --noinput
```

If you get and error, put down the container and remove volumnes with 
```
docker-compose down -v
```
Rebuild the container.

This project is based on [Michael Herman Tutorial](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/).