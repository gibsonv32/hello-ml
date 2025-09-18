.PHONY: setup test lint clean
setup:
\tconda env update -n ai311 -f environment.yml || true
test:
\tpython -m pytest -q
clean:
\trm -rf .pytest_cache **/__pycache__
