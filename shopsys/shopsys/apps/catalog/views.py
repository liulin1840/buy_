from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request, template_name):#request 前端请求对象
    page_title = '产品分类目录'
    return render(request, template_name, locals())#渲染模板

# 
def show_category(request, category_slug, template_name):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()# 对应着模板看
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render(request, template_name, locals())

#slug 唯一的,属于哪个分类
def show_product(request, product_slug, template_name):
    p = get_object_or_404(Product, slug=product_slug)#得到当前的产品
    categories = p.categories.filter(is_active=True) #属于那些分类的
    page_title = p.name                              #当前页面的标题
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render(request, template_name, locals())#渲染模板,