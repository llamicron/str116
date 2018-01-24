clean:
	rm -rf dist/
	rm -rf build/

build:
	python setup.py sdist

install: clean build
	pip install dist/*

upload: clean build install
	twine upload dist/*

test:
	pytest

install_deps:
	pip install -r requirements.txt
