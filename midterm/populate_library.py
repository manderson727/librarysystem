import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'midterm.settings')

import django
django.setup()
from library.models import Genre, Media, User

def populate():
    media = [
        {"type": "Book",
         "title": "Game of Thrones - A Song of Ice and Fire",
         "isbn": "0553593714"},
        {"type": "Book",
         "title": "Game of Thrones - A Storm of Swords",
         "isbn": "055357342X"},
        {"type": "Book",
         "title": "Game of Thrones - A Feast for Crows",
         "isbn": "055358202X"}
    ]

    cats = {"Fantasy": {"media": media}}

    for cat, cat_data in cats.items():
        c = add_genre(cat)
        for p in cat_data["media"]:
            add_media(c, p["type"], p["title"], p["isbn"])

    users = [
        {"name": "Mike Anderson",
         "email": "andersm3@lasalle.edu",
         "username": "manderson",
         "password": "unsecure"},
        {"name": "user2",
         "email": "user2@lasalle.edu",
         "username": "user2",
         "password": "unsecure"}
    ]

    for user in users:
        add_user(user["name"], user["email"], user["username"], user["password"])

def add_user(name, email, username, password):
    u = User.objects.get_or_create(name=name, email=email, username=username, password=password)[0]
    u.save()
    return u

def add_media(cat, type, title, isbn):
    p = Media.objects.get_or_create(genre=cat, type=type, title=title, isbn=isbn)[0]
    p.save()
    return p

def add_genre(name):
    c = Genre.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Library population script...")
    populate()
