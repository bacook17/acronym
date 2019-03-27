VERSION := $(shell python -c "import acronym; print(acronym.__version__)")

default: install

install:
	pip install . --upgrade

upload: install
	python setup.py sdist bdist_wheel
	twine upload dist/acronym-$(VERSION)*
