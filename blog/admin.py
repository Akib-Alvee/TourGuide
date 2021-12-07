from django.contrib import admin

from .models import Post, Tag


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    list_filter = ('tags', 'created_on', 'updated_on')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)} 
    autocomplete_fields = ('tags',)


admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    

admin.site.register(Tag, TagAdmin)