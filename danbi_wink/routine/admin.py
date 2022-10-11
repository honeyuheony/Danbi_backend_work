from django.contrib import admin
from .models import Day, Routine, Result

# Register your models here.
admin.site.register(Result)
admin.site.register(Routine)
admin.site.register(Day)