from django.contrib import admin

# Register your models here.
from tiny_migrate.models import OlympicSkier, OlympicCoach

admin.site.register(OlympicSkier)
admin.site.register(OlympicCoach)
