from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from blog.models import User, Keyword, Article, Content, Comment

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Keyword)
admin.site.register(Article)
admin.site.register(Content)
admin.site.register(Comment)
admin.site.unregister(Group)
