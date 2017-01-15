all: js

test:
	python -m unittest discover

js:
	npm run webpack

watch:
	npm run watch

clean:
	rm -rf ./public/dist/*

