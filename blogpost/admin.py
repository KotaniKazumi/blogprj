from django.contrib import admin

# Register your models here.
from .models import Smodel, BlogModel

admin.site.register(Smodel)
admin.site.register(BlogModel)
