.PHONY: default
default: check

.PHONY: format
format: white

.PHONY: white
white: black

.PHONY: black
black:
	white toothbrush toothbrush.py

.PHONY: lint
lint: requirements.txt setup.py
	tox -e lint
	tox -e pytype

.PHONY: test
test: requirements.txt setup.py
	tox

.PHONY: check
check: lint test

.PHONY: clean
clean:
	rm -f *.pyc
	rm -rf .tox
	rm -rf *.egg-info
	rm -rf __pycache__
	rm -f pip-selfcheck.json
	rm -rf pytype_output

.PHONY: pypi
pypi:
	rm -f dist/*.tar.gz
	python3 setup.py sdist
	twine upload dist/*.tar.gz

.PHONY: release
release:
	git diff-index --quiet HEAD --
	make check
	bumpversion patch
	git push --tags
	git push
	make pypi
