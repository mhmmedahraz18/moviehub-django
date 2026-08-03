from django.contrib import admin
from .models import Category, Movie


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "rating", "user")
    list_filter = ("category",)
    search_fields = ("title", "actors")