from django.contrib import admin
from blog.models import Post, Tag, Comment



class PostAdmin(admin.ModelAdmin):
    raw_id_fields = [
            'author',
            'likes',
            'tags',
        ]

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = [
    		'post',
            'author',
        ]
admin.site.register(Comment, CommentAdmin)


admin.site.register(Tag)
