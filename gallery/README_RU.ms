# Simple-gallery

## Введение
Простая галерея изображений, создана на Django и Channels.
Показ и загрузка изображений в директорию media/.

## Начало
Вам необходим git. Клонируйте этот репозиторий.

```
git clone https://github.com/Chukak/simple-gallery.git
```

### Требования
Вам необходимо установить python 3.6 или позднюю версию и pip 9.0.1.
Также нужен channels 2.0.

```
pip install -r requirements.txt
```

### Запуск проекта
Создайте миграции django.

``` python manage.py makemigrations ```

Migrate.

``` python manage.py migrate ```

Запустите сервер django.

``` python manage.py runserver ```

#### Суперпользователь
Этот проект имеет сайт администрации. Создайте суперпользователя с помощью команды:

``` python manage.py createsuperuser ```

## Авторы
[chukak](https://github.com/Chukak)