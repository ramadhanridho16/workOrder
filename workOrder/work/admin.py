from django.contrib import admin
from .models import Report, Pekerjaan, Pelaksana, Pengguna, Status
# Register your models here.

admin.site.register(Pekerjaan)
admin.site.register(Pelaksana)
admin.site.register(Pengguna)
admin.site.register(Status)
admin.site.register(Report)
