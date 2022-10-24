from django.contrib import admin
from .models import Beat, Producer, Comment

# Register your models here.
admin.site.register(Beat)
admin.site.register(Producer)
admin.site.register(Comment)