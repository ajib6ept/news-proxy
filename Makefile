
lint:
	poetry run flake8 news_proxy tests

run:
	poetry run python news_proxy/server_async.py

test:
	poetry run pytest -vvs