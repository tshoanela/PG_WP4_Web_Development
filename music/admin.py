from django.contrib import admin

from .models import Album
from .models import Song
#tell django that the album model should appear in the admin site page
admin.site.register(Album)
admin.site.register(Song)


