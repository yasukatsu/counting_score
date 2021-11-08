# 実行環境起動
up:
	docker-compose up -d
	docker-compose exec python3 bash

build:
	docker-compose up -d --build
	docker-compose exec python3 bash

# 実行環境削除
down:
	docker-compose down