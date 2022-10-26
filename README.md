# REST_calculator

Простой REST API калькулятор, реализованный с помощью фреймворка FastAPI.

## Содержание

- `Dockerfile` — докер-файл для сборки изображения.
- `requirements.txt` — список необходимых пакетов и их версии.
- `app` — директория с кодом приложения.
- `code` — рабочая директория докер-контейнера.

## Запуск приложения

- Переходим в рабочую директорию проекта.
- Запускаем docker.
- Выполняем команду `docker build -t myimage .`
- Выполняем команду `docker run -d --name mycontainer -p 80:80 myimage`
