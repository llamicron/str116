clean:
	rm -rf dist/
	rm -rf build/

build:
	python setup.py sdist

install: clean build
	pip install dist/*

upload: clean build install
	twine upload dist/*