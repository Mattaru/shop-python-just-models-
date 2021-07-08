from django.contrib import admin

from .models import Category, Order, Product, Refund


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'user',
        'received',
    )
    search_fields = ('user',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'quantity',
        'discount',
        'price',
        'on_warehouse',
    )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'order_number',
        'accepted',
    )
    search_fields = ('user',)
