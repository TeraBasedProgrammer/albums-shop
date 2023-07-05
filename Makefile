# Usage: make <command>

# Run django server
run:
	python manage.py runserver 8000

# Run django python shell
shell:
	python manage.py shell -i ipython

# Create django migrations
makemigr:
	python manage.py makemigrations

# Migrate django migrations
migrate:
	python manage.py migrate

# Fill up django db
setupdb:
	python manage.py setup-db

# Clear django db custom models
resetdb:
	python manage.py reset-db
