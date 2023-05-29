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

`pip install -r requirements.txt`\
`python manage.py makemigrations`\
`python manage.py migrate`


## Configuration of the path to the npm executable
Tailwind CSS requires Node.js to be installed on your machine. Node.js is a JavaScript runtime that allows you to run JavaScript code outside the browser. Most (if not all) of the current frontend tools depend on Node.js.

If you don’t have Node.js installed on your machine, please follow installation instructions from the official Node.js page.

Sometimes (especially on Windows), the Python executable cannot find the npm binary installed on your system. In this case, you need to set the path to the npm executable in settings.py file manually (Linux/Mac):

`NPM_BIN_PATH = '/usr/local/bin/npm'`

On Windows it might look like this:

`NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"`
Please note that the path to the npm executable may be different for your system. To get the npm path, try running the command `which npm` in your terminal.

Then run 

`python manage.py tailwind start`\
`python manage.py runserver`


## For Production Build

`python manage.py tailwind build` \
`python manage.py collectstatic`

## Deploy to Digital Ocean
Here are the general steps to deploy a Django app to Digital Ocean. Detailed instructions are outside the scope of this README and can be found in the official Digital Ocean documentation and Django deployment guides.

1. Create a new droplet on Digital Ocean. Choose an image that includes Django or set up the necessary environment yourself.

2. Upload your Django project to the droplet. You can do this using a variety of methods, such as Git, SCP, or FTP.

3. Set up the database. Django supports several databases. The choice will depend on your needs and the resources available on your droplet.

4. Configure the Django project for production. This will include tasks such as setting DEBUG = False in your settings file, configuring your ALLOWED_HOSTS, and setting up static and media files to be served properly.

5. Set up a web server. Common choices for Django projects are Gunicorn or uWSGI.

6. Set up a reverse proxy. This is typically Nginx or Apache, which will handle static files and pass other requests to the Django app.

7. Start your Django app. This usually involves running the web server configured in step 5.

8. Visit your droplet's IP address in a web browser to confirm everything is working.


### You can follow this tutorial to successfully deploy it 
[Youtube tutorial](https://www.youtube.com/watch?v=W_nqdc6IMDw)

[Written tutorial](https://www.codewithmuh.com/blog/deploy-django-project-on-digital-ocean-vps-droplet)

[Digital Ocean turorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04) - This will help you in setting up the postgres database.

## Preconfigured Packages

Includes preconfigured packages to kick start Django-Authentication by just setting appropriate configuration.

| Package                                                      | Usage                                                            |
| ------------------------------------------------------------ | ---------------------------------------------------------------- |
| [django-allauth](https://django-allauth.readthedocs.io/en/latest/)        | Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.           |
| [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) | django-crispy-forms provides you with a `crispy` filter and `{% crispy %}` tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way.     |


## License

This project is licensed under the terms of the MIT license.
