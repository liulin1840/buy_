from django.contrib import admin

from .models import Category, Product
from .forms import ProductAdminForm


@admin.register(Product)#装饰器,注册相关函数
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    # 设置admin界面如何显示产品列表
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)#那个有连接
    list_per_page = 50            #一页显示多少条
    ordering = ['-created_at']    #
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)  #不包含选项
    prepopulated_fields = {'slug': ('name',)} #映射 自动填充


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('name',)}  