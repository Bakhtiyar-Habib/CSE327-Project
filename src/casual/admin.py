from django.contrib import admin

# Register your models here.
from .models import CasualMenT

admin.site.register(CasualMenT)

from .models import CasualWomenT

admin.site.register(CasualWomenT)

from .models import CasualMenPant

admin.site.register(CasualMenPant)

from .models import CasualWomenPant

admin.site.register(CasualWomenPant)