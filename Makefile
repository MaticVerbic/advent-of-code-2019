container := docker-compose run --name advent --rm container
run:
	$(container) python3 /files/run.py run
test:
	$(container) python3 /files/run.py test
day-one:
	$(container) python3 /files/day_1/run.py
day-two:
	$(container) python3 /files/day_2/run.py
day-three:
	$(container) python3 /files/day_3/run.py
day-four:
	$(container) python3 /files/day_4/run.py
day-five:
	$(container) python3 /files/day_5/run.py
day-six:
	$(container) python3 /files/day_6/run.py
