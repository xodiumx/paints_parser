# test_parser

## Установка через docker
1. Клонируйте репозиторий
```
git clone git@github.com:xodiumx/test_parser.git
```
3. Перейдите в директорию
```
cd src
```
2. В директории `scr` создайте `.env` file
```
DB_NAME=ordernn
DB_HOST=db_parser
# DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=admin

POSTGRES_USER=postgres
POSTGRES_PASSWORD=admin

PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin
```
3. Выполните команду
```
docker-compose up -d
```