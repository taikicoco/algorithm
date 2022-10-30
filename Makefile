build:
	docker-compose build
up:
	docker-compose up -d --build
bash:
	docker-compose exec python3 bash
down:
	docker-compose down