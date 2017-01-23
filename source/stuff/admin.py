from django.contrib import admin

from stuff.models import Item, Category, Container

class itemAdmin(admin.ModelAdmin):
    class Meta:
        model = Item

    list_display = [
        "id",
        "category",
        "description",
    ]

    list_display_links = ['description',]

class categoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

    list_display = [
        "id",
        "title",
        "description",
        "sortOrder",
    ]

    list_display_links = ['title',]

    ordering = ["sortOrder", "title"]

class containerAdmin(admin.ModelAdmin):
    class Meta:
        model = Container

    list_display = [
        "id",
        "title",
        "description",
        "sortOrder",
    ]

    list_display_links = ['title',]

    ordering = ["sortOrder", "title"]


admin.site.register(Item, itemAdmin)
admin.site.register(Category, categoryAdmin)
admin.site.register(Container, containerAdmin)
