import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'midterm.settings')

import django
django.setup()
from library.models import Topic, Media

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

    cats = {"Fantasy": {"topics": media}}

    for cat, cat_data in cats.items():
        c = add_topic(cat)
        for p in cat_data["topics"]:
            add_media(c, p["type"], p["title"], p["isbn"])

def add_media(cat, type, title, isbn):
    p = Media.objects.get_or_create(topic=cat, type=type, title=title, isbn=isbn)[0]
    p.save()
    return p

def add_topic(name):
    c = Topic.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Library population script...")
    populate()
