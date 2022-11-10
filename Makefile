
lint:
	poetry run flake8 news_proxy tests

mypy:
	poetry run mypy --strict .

run:
	poetry run news-proxy

test:
	poetry run pytest -vvs