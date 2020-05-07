from django.contrib import admin

# Register your models here.
from .models import FormalMen

admin.site.register(FormalMen)

from .models import FormalWomen

admin.site.register(FormalWomen)