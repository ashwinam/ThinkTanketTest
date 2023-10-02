from django.contrib import admin
from .models import HobbiesTbl, UserTbl, AgeTbl

# Register your models here.
admin.site.register(HobbiesTbl)
admin.site.register(UserTbl)
admin.site.register(AgeTbl)