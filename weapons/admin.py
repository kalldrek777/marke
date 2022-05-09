import time

from django.contrib import admin
from weapons.models import Product
from django_object_actions import DjangoObjectActions
import os

import subprocess


class ProductAdmin(DjangoObjectActions, admin.ModelAdmin):
    exclude = ['img', 'num_product']
    list_display = ['name', 'link_product']

    def save_model(self, request, obj, form, change):
        qs = Product.objects.all()
        num = 1
        for i in qs:
            num += 1
        print(num)
        obj.num_product = num
        super().save_model(request, obj, form, change)

    def get(modeladmin, request, queryset):
        os.system('scrapy crawl market77')

    changelist_actions = ('get',)


admin.site.register(Product, ProductAdmin)















