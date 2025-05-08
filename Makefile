.PHONY: check

check:
	ruff check . --fix
	black .
