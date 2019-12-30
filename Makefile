container := docker-compose run --name advent --rm container
run:
	$(container) python3 /files/run.py 
day-one:
	$(container) python3 /files/day_1/run.py
day-two:
	$(container) python3 /files/day_2/run.py
day-three:
	$(container) python3 /files/day_3/run.py
day-four:
	$(container) python3 /files/day_4/run.py
