from django.contrib import admin

# Register your models here.
from .models import Add_guide
from .models import Add_hotel
from .models import Add_package
from .models import Add_place

admin.site.register(Add_guide)
admin.site.register(Add_hotel)
admin.site.register(Add_package)
admin.site.register(Add_place)