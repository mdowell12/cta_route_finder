all: js

test:
	python -m unittest discover

js:
	cd public/build; webpack --display-error-details

watch:
	cd public/build; webpack --display-error-details --progress --colors --watch

clean:
	rm -rf ./public/dist/*

