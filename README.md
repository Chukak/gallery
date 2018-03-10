# Simple-gallery

## Documentations
[Русский](https://github.com/Chukak/gallery/blob/master/gallery/README_RU.md)

## Introduction
This is a simple gallery images, created on Django and Channels.
Show and upload images in media/ directory.

## Getting started
You needs git. Clone this repository.

```
git clone https://github.com/Chukak/simple-gallery.git
```

### Requirements
You needs to install python 3.6 or latest version and pip 9.0.1.
Also you need channels 2.0+.

```
pip install -r requirements.txt
```

### Start project
Make django migrations.

``` python manage.py makemigrations ```

Migrate.

``` python manage.py migrate ```

Run django server

``` python manage.py runserver ```

#### Superuser
This project has admin site. Create superuser command:

``` python manage.py createsuperuser ```

And check admin/ url.

## Author
[chukak](https://github.com/Chukak)
