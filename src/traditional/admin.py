from django.contrib import admin

# Register your models here.
from .models import TraditionalMen

admin.site.register(TraditionalMen)

from .models import TraditionalWomen

admin.site.register(TraditionalWomen)