from django.contrib import admin
from .models import Team # the . specifies that this is our models not the django version (but it would be django.db.models so not a big deal)

# Register your models here.
admin.site.register(Team)