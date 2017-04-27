from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField("名称", max_length=50)
    slug = models.SlugField(
        "Slug",
        max_length=50, unique=True,
        help_text='根据name生成的，用于生成页面URL，必须唯一')
    description = models.TextField("描述")
    is_active = models.BooleanField("是否激活", default=True)#是否激活
    meta_keywords = models.CharField(
        "Meta 关键词", max_length=255,
        help_text='meta关键词，有利于SEO， 用逗号分隔')
    meta_description = models.CharField(
        "Meta 描述", max_length=255,
        help_text='meta描述')
   	#有利于seo
    created_at = models.DateTimeField("创建时间", auto_now_add=True)#默认参数,自动创建
    updated_at = models.DateTimeField("更新时间", auto_now=True)#自动更新

    #子类,定义当前model的属性,
    class Meta:
        db_table = 'categories'#db name
        ordering = ['-created_at']#排序,降序排列
        verbose_name_plural = 'Categories'#复数变形

    #内置函数,复写了,显示实例的名称
    def __str__(self):
        return self.name
    # 如何使用?
    def get_absolute_url(self):
        return reverse('catalog_category', args=(self.slug,))


class Product(models.Model):
    name = models.CharField("名称", max_length=255, unique=True)
    slug = models.SlugField(
        "Slug",
        max_length=255, unique=True,
        help_text='根据name生成的，用于生成页面URL，必须唯一')
    brand = models.CharField("品牌", max_length=50)
    sku = models.CharField("计量单位", max_length=50)
    price = models.DecimalField("价格", max_digits=9, decimal_places=2)#不损失精度,最大9
    #可能有多个价格,促销原因
    old_price = models.DecimalField(
        "旧价格",
        max_digits=9, decimal_places=2, blank=True, default=0.00)
    image = models.ImageField("图片", max_length=50, upload_to='products')
    
    is_active = models.BooleanField("设为激活", default=True)
    is_bestseller = models.BooleanField("标为畅销", default=False)
    is_featured = models.BooleanField("标为推荐", default=False)
    
    quantity = models.IntegerField("数量")
    description = models.TextField("描述")
    meta_keywords = models.CharField(
        "Meta关键词",
        max_length=255, help_text='meta 关键词标签, 逗号分隔')
    meta_description = models.CharField(
        "Meta描述",
        max_length=255, help_text='meta 描述标签')
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_product', args=(self.slug,))

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None