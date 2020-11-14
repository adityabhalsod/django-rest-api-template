## Quick start for beginning

---

- # Basic settings

- First rename the file of remove postfix `.example` from `{{ project_name }}` folder and set your own config settings.

- Supported `Database`.
    1. Postgrages

# 1. ".ENV" environment

- The value of a variable is the first of the values defined in the following list:
    - Value of that variable in the .env file.
    - Value of that variable in the environment.
    - Default value, if provided.
    - Empty string.

    ``` shell
    CONFIG_PATH=${HOME}/.config/foo
    DOMAIN=example.org
    EMAIL=admin@${DOMAIN}
    DEBUG=${DEBUG:-false}
    ```

- At this point, parsed `key/value` from the `.env` file is now present as system environment variable and they can be conveniently accessed via `os.getenv()`:

``` shell
# settings.py
import os
SECRET_KEY = os.getenv("EMAIL")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
```

Note :  More information about `.env` goto [here.](https://github.com/theskumar/python-dotenv)

---

# 2. Seeding a database is a process using seed command

 - Seeding a database is a process in which an initial set of data is provided to a database when it is being installed. It is especially useful when we want to populate the database with data we want to develop in future. This is often an automated process that is executed upon the initial setup of an application. The data can be dummy data or necessary data such as an initial administrator account.
 
```shell
python manage.py seed
```
---

# 3. Deploy project ngix (gunicorn)

- Where `WSGI_APP` is of the pattern `$(MODULE_NAME):$(VARIABLE_NAME)`. The module name can be a full dotted path. 

```shell
gunicorn -c setup.ini {{ project_name }}.wsgi
```
Note :  More information about `gunicorn` goto [here.](https://docs.gunicorn.org/en/latest/index.html)

---

# 4. Swagger integration for api documentation

 ```Simplify API development for users, teams, and enterprises with the Swagger open source and professional toolset. Find out how Swagger can help you design and document your APIs at scale.```

- ## <span style="font-weight:bolder;">Features</span>
- full support for nested Serializers and Schemas
- response schemas and descriptions
- model definitions compatible with codegen tools
- customization hooks at all points in the spec generation process
- JSON and YAML format for spec
- bundles latest version of swagger-ui and redoc for viewing the - - generated documentation
- schema view is cacheable out of the box
- generated Swagger schema can be automatically validated by swagger-spec-validator
- supports Django REST Framework API versioning with `URLPathVersioning` and `NamespaceVersioning;` other DRF or custom versioning schemes are not currently supported

```shell
http://localhost:8000/swagger/
```
Note :  More information about `swagger` goto [here.](https://drf-yasg.readthedocs.io/en/stable/)

---
