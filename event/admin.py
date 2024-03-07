from django.contrib import admin
from .models import Event
# from .models import Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Event)
# admin.site.register(Review)

