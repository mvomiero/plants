build:
# just to build the image
	docker build -t postgres-database-image .

run:
	docker run -d --name postgres-database-container -p 5432:5432 --env-file ../.env postgres-database-image



