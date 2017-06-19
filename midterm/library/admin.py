from django.contrib import admin
from library.models import Genre, Media, MediaInstance, User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email')

admin.site.register(User, UserAdmin)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'isbn', 'genre')

@admin.register(MediaInstance)
class MediaInstance(admin.ModelAdmin):
    pass

@admin.register(Genre)
class Genre(admin.ModelAdmin):
    pass
