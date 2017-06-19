from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Genre'

    def __str__(self):
        return self.name

class Media(models.Model):
    title = models.CharField(max_length=128)
    isbn = models.CharField(max_length=128)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=128)
    image = models.ImageField(upload_to = 'static/images/')

    class Meta:
        verbose_name_plural = 'Media'

    def __str__(self):
        return self.title

class MediaInstance(models.Model):
    media = models.ForeignKey('Media', on_delete=models.SET_NULL, null=True)
    due = models.DateField(null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.media.title

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
