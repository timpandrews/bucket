from django.contrib import admin

from stuff.models import Item

class itemAdmin(admin.ModelAdmin):
    class Meta:
        model = Item

    list_display = [
        "id",
        "category",
        "description",
    ]




admin.site.register(Item, itemAdmin)
