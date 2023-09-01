from django.contrib import admin
from .models import Post,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)} # make the url of post match the title in slug format 
    list_filter = ('status', 'created_on')# creates a section in admin to filter content based on created on 
    summernote_fields = ('content')# summer not gives more design option on input fields when entering text in content field admin panel


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','post','approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


