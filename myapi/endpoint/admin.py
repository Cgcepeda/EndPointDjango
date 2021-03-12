from django.contrib import admin
from .models import Reviews, PropertyTypes, States, Cities, Categories, Properties, Transaction
# Register your models here.
admin.site.register(Reviews)
admin.site.register(Transaction)
admin.site.register(PropertyTypes)
admin.site.register(States)
admin.site.register(Cities)
admin.site.register(Categories)
admin.site.register(Properties)