import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'midterm.settings')

import django
django.setup()
from library.models import Genre, Media, User, SubGenre, MediaInstance

def populate():

    genres = [
        {"name": "Fantasy"}
    ]

    for genre in genres:
        add_genre(genre["name"])

    subgenres = [
        {"name": "Sword and Sorcery",
         "genre_id": 1},
        {"name": "Mythic Fiction",
         "genre_id": 1}
    ]

    for subgenre in subgenres:
        add_subgenre(subgenre["name"], subgenre["genre_id"])

    medias = [
        {"type": "Book",
         "title": "Game of Thrones - A Song of Ice and Fire",
         "isbn": "0553593714",
         "image": "static/images/song.jpg",
         "genre_id": 1,
         "subgenre_id": 1},
        {"type": "Book",
         "title": "Game of Thrones - A Storm of Swords",
         "isbn": "055357342X",
         "image": "static/images/storm.jpg",
         "genre_id": 1,
         "subgenre_id": 2},
        {"type": "Book",
         "title": "Game of Thrones - A Feast for Crows",
         "isbn": "055358202X",
         "image": "static/images/feast.jpg",
         "genre_id": 1,
         "subgenre_id": 2}
    ]

    for media in medias:
        add_media(media["type"], media["title"], media["isbn"], media["image"], media['genre_id'], media["subgenre_id"])
    #cats = {"Fantasy": {"media": media}}

    #for cat, cat_data in cats.items():
    #    c = add_genre(cat)
    #    for p in cat_data["media"]:
    #        add_media(c, p["type"], p["title"], p["isbn"], p["image"], p["subgenre_id"])

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

    mediainstances = [
        {"media_id": 1,
         "user_id": 1,
         "due": "2017-06-19"},
        {"media_id": 2,
         "user_id": 2,
         "due": "2017-07-19"},
        {"media_id": 3,
         "user_id": 2,
         "due": "2017-06-1"}
    ]

    for mediainst in mediainstances:
        add_mediainst(mediainst["media_id"], mediainst["user_id"], mediainst["due"])

def add_user(name, email, username, password):
    u = User.objects.get_or_create(name=name, email=email, username=username, password=password)[0]
    u.save()
    return u

def add_media(type, title, isbn, image, genre_id, subgenre_id):
    p = Media.objects.get_or_create(type=type, title=title, isbn=isbn, image=image, genre_id=genre_id, subgenre_id=subgenre_id)[0]
    p.save()
    return p
#def add_media(cat, type, title, isbn, image, subgenre_id):
#    p = Media.objects.get_or_create(genre=cat, type=type, title=title, isbn=isbn, image=image, subgenre_id=subgenre_id)[0]
#    p.save()
#    return p

def add_genre(name):
    c = Genre.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_subgenre(name, genre_id):
    s = SubGenre.objects.get_or_create(name=name, genre_id=genre_id)[0]
    s.save()
    return s

def add_mediainst(media_id, user_id, due):
    m = MediaInstance.objects.get_or_create(media_id=media_id, user_id=user_id, due=due)[0]
    m.save()
    return m

if __name__ == '__main__':
    print("Starting Library population script...")
    populate()
