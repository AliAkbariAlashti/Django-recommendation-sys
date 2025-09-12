from django.contrib import admin
from .models import user, movies, UserInterests
# Register your models here.


admin.site.register(user)
admin.site.register(movies)
admin.site.register(UserInterests)