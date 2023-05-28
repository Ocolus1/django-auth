# Django-Authentication

A simple Boilerplate to Setup Authentication using Django-allauth and tailwind, with a custom template for login and registration.

## Getting Started

### Prerequisites

- Python 3.8.6 or higher

### Project setup

```sh
# clone the repo
$ git clone https://github.com/Ocolus1/django-auth.git

# move to the project folder
$ cd django-auth
```

### Creating virtual environment

- Create a `virtual environment` for this project:

```shell
# creating pipenv environment for python 3
$ virtualenv venv

# activating the pipenv environment
$ cd venv/bin #windows environment you activate from Scripts folder

# if you have multiple python 3 versions installed then
$ source ./activate
```

### Configured Enviromment

#### Environment variables

```shell
SECRET_KEY = #random string
DEBUG = #True or False
ALLOWED_HOSTS = #localhost
DATABASE_NAME = #database name (You can just use the default if you want to use SQLite)
DATABASE_USER = #database user for postgres
DATABASE_PASSWORD = #database password for postgres
DATABASE_HOST = #database host for postgres
DATABASE_PORT = #database port for postgres
ACCOUNT_EMAIL_VERIFICATION = #mandatory or optional
EMAIL_BACKEND = #email backend
EMAIL_HOST = #email host
EMAIL_HOST_PASSWORD = #email host password
EMAIL_USE_TLS = # if your email use tls
EMAIL_PORT = #email port
```

> change all the environment variables in the `.env.template` and don't forget to rename it to `.env`.


## Project Structure
The Django project is organized into the following main directories:

`config`: This directory contains the main project settings and entry points. It includes the settings.py file and the root URL configuration.

`accounts`: This directory contains authentication models, including a custom user model and email-based account flow. It also contains the account URL configuration, form styles and company models.

`pages`: This directory is where the main user-facing elements of the web app should go.

`theme`: This directory is where the main tailwind configurations of the web app should go.


### Run the project

After Setup the environment, you can run the project using the `Makefile` provided in the project folder.

```makefile
help:
 @echo "Targets:"
 @echo "    make install" #install requirements
 @echo "    make makemigrations" #prepare migrations
 @echo "    make migrations" #migrate database
 @echo "    make createsuperuser" #create superuser
 @echo "    make run_server" #run the server
 @echo "    make lint" #lint the code using black
 @echo "    make test" #run the tests using Pytest
```

`pymake install`
`pymake makemigrations`
`pymake migrations`
`pymake run_server`


## Preconfigured Packages

Includes preconfigured packages to kick start Django-Authentication by just setting appropriate configuration.

| Package                                                      | Usage                                                            |
| ------------------------------------------------------------ | ---------------------------------------------------------------- |
| [django-allauth](https://django-allauth.readthedocs.io/en/latest/)        | Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.           |
| [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) | django-crispy-forms provides you with a `crispy` filter and `{% crispy %}` tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way.     |


## License

This project is licensed under the terms of the MIT license.
