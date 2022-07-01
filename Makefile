install:
	#install cammands 
	pip install --upgrade pip && \
	pip install -r requirements.txt 
run_python:
	#run textblob
	python -m textblob.download_corpora
format:
	#format code
	black *.py mylib/*.py 
lint:
	#flake8 or pylint 
	pylint --disable=R,C *.py mylib/*.py 
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main test_*.py 
build:
	#build container 
	docker build -t fastapi .
run:
	#run container
	docker run -p 127.0.0.1:8282:8282 fastapi
	
deploy:
	#deploy
all: install format lint test deploy