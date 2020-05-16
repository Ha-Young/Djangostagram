from django.contrib import admin
from .models import Dsuser

# Register your models here.


class DsuserAdmin(admin.ModelAdmin):
    list_display=('user_id', 'password', 'email', 'registered_dttm')

admin.site.register(Dsuser, DsuserAdmin)