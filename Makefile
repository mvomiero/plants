start_db:
	pg_ctl -D /opt/homebrew/var/postgresql@14 start

stop_db:
	pg_ctl -D /opt/homebrew/var/postgresql@14 stop

# venv commands seem not to work here

stop_venv:
	deactivate

start_venv:
	. venv/bin/activate

run_background:
	nohup python3 main.py
	

docker_build:
	make -C Docker build

docker_run:
	make -C Docker run