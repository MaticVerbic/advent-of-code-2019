container := docker-compose run --name advent --rm container
run:
	$(container) python3 /files/run.py 
day-one:
	$(container) python3 /files/day_1/run.py
day-two:
	$(container) python3 /files/day_2/run.py
