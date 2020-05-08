from django.contrib import admin

# Register your models here.
from .models import DenimMen

admin.site.register(DenimMen)

from .models import DenimWomen

admin.site.register(DenimWomen)