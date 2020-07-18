SOURCE_VERSION = $(shell git describe --long --always --exclude '*')

.PHONY: clean

default: usage

usage:
	@echo "USAGE:"
	@echo "   make command [options]"
	@echo
	@echo "COMMANDS:"
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed 's/^/   /' | sed -e 's/\\$$/AA/' | sed -e 's/#//g' | column -t -s ":" | sort -k1

rm_pyc: ### clear pyc
	@find . -iname '*.pyc' -delete
	@find . -iname '__pycache__' -delete

dist_clean: ### dist clean
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info
	@rm -rf .eggs/
	@rm -rf .pytest_cache

clean: dist_clean rm_pyc  ### rm_pyc and dict clean

test:  ### tests
	pytest -vvv

dist: clean  ### build dist package (after clean)
	python3 setup.py sdist
	python3 setup.py bdist_wheel

version: dist  ### version
	python3 setup.py --version

license: dist  ### some license stufff
	python3 setup.py --license