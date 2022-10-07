from django.contrib import admin
from .models import Routine_day, Routine, Routine_result

# Register your models here.
admin.site.register(Routine_result)
admin.site.register(Routine)
admin.site.register(Routine_day)