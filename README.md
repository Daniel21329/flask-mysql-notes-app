# Flask Notes App с MySQL и Adminer

## Структура
- backend/ - Flask приложение с Dockerfile  
- docker-compose.yml - дефинира 3 услуги: backend, db (MySQL), adminer  
- README.md - документация

## Стартиране
1. Клонирайте репото  
2. Стартирайте с: docker-compose up --build
3. Посетете http://localhost:5000 за записки  
4. Админер е на http://localhost:8080 (логин: root, парола: password, база: notesdb)

## Услуги
- backend: Flask приложение  
- db: MySQL база  
- adminer: уеб клиент за MySQL

## Комуникация
Flask приложението се свързва с MySQL през hostname `db` в docker мрежата.
