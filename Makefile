install:
	poetry install

run:
	poetry run fastapi dev src/main.py

test:
	poetry run pytest . -v
