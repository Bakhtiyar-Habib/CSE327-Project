from django.contrib import admin

# Register your models here.
from .models import Brands

admin.site.register(Brands)

from .models import Brands_detail

admin.site.register(Brands_detail)