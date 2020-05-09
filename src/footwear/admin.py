from django.contrib import admin

# Register your models here.
from .models import FootwearMen

admin.site.register(FootwearMen)

from .models import FootwearWomen

admin.site.register(FootwearWomen)