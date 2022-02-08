install-local:
	pip install -r local-requirements.txt
install:
	pip install -r requirements.txt
test:
	python -m pytest -vv test_main.py
lint:
	pylint --disable=R,C main.py
all:
	install lint test