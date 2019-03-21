from django.contrib import admin
from .models import Company,Post

# Register your models here.
"""
公司后台admin,
后台显示字段为公司名称'name'和公司简介'info'
"""


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # 后台显示字段name,info
    list_display = ('name', 'info',)


#删除页显示——艾鹏
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content',)