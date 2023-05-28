help:
	@echo "Targets:"
	@echo "    make install"
	@echo "    make makemigrations"
	@echo "    make migrations"
	@echo "    make createsuperuser"
	@echo "    make run_server"
	@echo "    make lint"
	@echo "    make test"

install:
	@echo "Installing..."
	pip install -r requirements.txt

migrations:
	@echo "Running migrations..."
	python manage.py makemigrations

migrate:
	@echo "Migrating..."
	python manage.py migrate

createsuperuser:
	@echo "Creating user..."
	python manage.py createsuperuser

run_server:
	@echo "Running server..."
	python manage.py runserver

lint:
	@echo "Linting..."
	black --target-version=py38

test:
	@echo "Running tests..."
	pytest --cov=. --cov-report=html