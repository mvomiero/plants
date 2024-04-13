run:
	python3 main.py

# venv commands seem not to work here
stop_venv:
	deactivate

start_venv:
	. venv/bin/activate

run_background:
	nohup python3 main.py
	

up:
	make -C Docker up

down:
	make -C Docker down

start_db:
	brew services start postgresql