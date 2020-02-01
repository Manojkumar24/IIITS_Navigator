from django.contrib import admin
from .models import Events, Professor, Classes, Rooms
# Register your models here.
admin.site.register([Events, Professor, Classes, Rooms])
