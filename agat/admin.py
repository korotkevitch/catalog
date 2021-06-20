from django.contrib import admin


from .models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'text', 'slug', 'image_preview', 'icon_code')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Service, ServiceAdmin)


from .models import About
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'text', 'image_preview')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(About, AboutAdmin)


from .models import Price
class PriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'price_item', 'price', 'price_content', 'image_preview')
    prepopulated_fields = {'slug': ('price_item',)}
admin.site.register(Price, PriceAdmin)


from .models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'description', 'id', 'slug', 'image_preview', 'icon_code')
    prepopulated_fields = {'slug': ('cat_name',)}
admin.site.register(Category, CategoryAdmin)


from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'id', 'category', 'subcategory', 'prefix', 'price', 'description', 'slug', 'image_preview',)
    prepopulated_fields = {'slug': ('product_name',)}
admin.site.register(Product, ProductAdmin)


from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message')
admin.site.register(Contact, ContactAdmin)


from .models import FeedbackPhone
class FeedbackPhoneAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'phone')
admin.site.register(FeedbackPhone, FeedbackPhoneAdmin)
