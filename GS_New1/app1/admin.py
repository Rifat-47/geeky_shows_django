from django.contrib import admin
from .models import Blog, Author, Entry
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

class EntryAdmin(admin.ModelAdmin):
    list_display = ['blog', 'headline', 'pub_date', 'mod_date', 'file']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Entry, EntryAdmin)