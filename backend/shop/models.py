import uuid

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


def get_img_upload_path(instance, filename):
    """Make new path for the files uploading."""
    return f'product-images/{instance.name}/{filename}'


class Category(models.Model):
    name = models.CharField(_('name'), max_length=255, blank=True)
    slug = models.CharField(_('slug'), max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug and self.name:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(_('name'), max_length=255, blank=True)
    brand = models.CharField(_('brand'), max_length=255, blank=True)
    description = models.TextField(_('description'), default='')
    img = models.ImageField(_('product image'), upload_to=get_img_upload_path, default='unknown.png',)
    slug = models.CharField(_('slug'), max_length=255, blank=True, null=True, unique=True)
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name='products', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    quantity = models.IntegerField(_('quantity'))
    sold = models.IntegerField(_('sold'), default=0)
    price = models.DecimalField(_('price'), max_digits=5, decimal_places=2)
    discount = models.IntegerField(_('discount'), default=0)
    on_warehouse = models.BooleanField(_('on warehouse'), default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug and self.name:
            self.slug = slugify(self.name)

        # For checking quantity on the warehouse
        # Need test
        if self.quantity > 0:
            self.on_warehouse = True

        return super().save(*args, **kwargs)


class Order(models.Model):
    order_number = models.UUIDField(_('order number'), default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, verbose_name=_('user'), on_delete=models.SET_NULL, blank=True, null=True)
    products = models.ManyToManyField(Product, verbose_name=_('products'), blank=True)
    start_date = models.DateTimeField(_('order date'), auto_now_add=True)
    ordered_date = models.DateTimeField(_('order date'), blank=True, null=True)
    # payment = models.ForeignKey()
    # shipping_address = models.ForeignKey()
    # billing_address = models.ForeignKey()
    being_delivered = models.BooleanField(_('being delivered'), default=False)
    received = models.BooleanField(_('received'), default=False)
    refund_requested = models.BooleanField(_('refund requested'), default=False)
    refund_granted = models.BooleanField(_('refund granted'), default=False)

    def __str__(self):
        return f'{self.order_number}'


class Refund(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'), on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.UUIDField(blank=True, null=True)
    request_date = models.DateTimeField(_('order date'), auto_now_add=True)
    reason = models.TextField(_('reason'), blank=True)
    accepted = models.BooleanField(_('accepted'), default=False)
