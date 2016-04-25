from django.contrib import admin
from aiwars.models import Game
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Game)