
install:
	poetry install

lint:
	poetry run flake8 news_proxy tests

mypy:
	poetry run mypy --strict .

run:
	poetry run news-proxy

test:
	poetry run pytest -vvs

test_coverage:
	poetry run coverage run --source=news_proxy -m pytest tests
	poetry run coverage xml
	poetry run coverage report