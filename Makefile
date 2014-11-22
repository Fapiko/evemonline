SHELL=/bin/bash

virtualenv:
	virtualenv env; \
	source env/bin/activate; \
	pip install -r requirements.txt; \
