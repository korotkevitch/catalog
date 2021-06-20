from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.shortcuts import reverse


class About(models.Model):
    title = models.CharField('Название в шапке', max_length=50, blank=True)
    subtitle = models.CharField('Подзаголовок перед текстом', max_length=70, blank=True)
    text = models.TextField('Описание')
    slug = models.SlugField(max_length=70, unique=True)
    image = models.FileField('Фото', blank=True)

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'

    def __str__(self):
        return self.title

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:30px;" />' % self.image.url)
        else:
            return 'Нет фото'

    image_preview.short_description = 'Фото'


class Price(models.Model):
    title = models.CharField('Название раздела', max_length=50, blank=True)
    subtitle = models.CharField('Подраздел', max_length=30, blank=True)
    price_item = models.CharField('Тариф', max_length=30, blank=True)
    price_content = models.TextField('Описание тарифа', blank=True)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=6)
    slug = models.SlugField(max_length=70, unique=True)
    image = models.FileField('Фото', blank=True)

    class Meta:
        verbose_name = 'Прайс-лист'
        verbose_name_plural = 'Прайс-лист'

    def __str__(self):
        return self.title

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.image.url)
        else:
            return 'Нет фото'

    image_preview.short_description = 'Фото'


class Contact(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    message = models.TextField('Сообщение', max_length=500, blank=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.name


class FeedbackPhone(models.Model):
    date_time = models.DateTimeField("Дата", default=datetime.now, blank=True,)
    phone = models.CharField('Телефон', max_length=50, blank=True, )

    class Meta:
        verbose_name = 'Просьба позвонить'
        verbose_name_plural = 'Просьбы позвонить'

    def __str__(self):
        return self.phone


class Service(models.Model):
    title = models.CharField('Название в шапке', max_length=50, blank=True)
    subtitle = models.CharField('Подзаголовок перед текстом', max_length=70, blank=True)
    text = models.TextField('Описание')
    slug = models.SlugField(max_length=70, unique=True)
    icon_code =  models.CharField('Флатикон', max_length=50, blank=True)
    image = models.FileField('Фото', blank=True)

    def get_absolute_url(self):
        return reverse('service', kwargs={'service': self.slug})   # в маршруте 'service' вместо <service> ставится slug

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:30px;" />' % self.image.url)
        else:
            return 'Нет фото'

    image_preview.short_description = 'Фото'


class Catalog(models.Model):  # Перечень категорий (Кресты, Венки...)
    catalog_name = models.CharField('Название', max_length=50, blank=True)
    text = models.TextField('Вступление')
    slug = models.SlugField(max_length=70, unique=True)

    def get_absolute_url(self):
        return "/catalog/"

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'

    def __str__(self):
        return self.catalog_name


class Category(models.Model):
    cat_name = models.CharField('Категория', max_length=50, blank=True)
    description = models.CharField('Описание для Главной', max_length=70, blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    image = models.FileField('Фото', blank=True)
    icon_code = models.CharField('Код флатикона', max_length=30, blank=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category': self.slug})


    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'Нет фото'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    subcategory = models.CharField('Подкатегория', max_length=30, blank=True)
    prefix = models.CharField('Префикс', max_length=30, blank=True)  # для фильтра в шаблоне Category
    product_name = models.CharField('Название', max_length=70, blank=True)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=6)
    description = models.TextField('Описание', blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    image = models.FileField('Фото', blank=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'category': self.category.slug, 'product': self.slug })

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.image.url)
        else:
            return 'Нет фото'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.product_name


