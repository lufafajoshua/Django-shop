# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#import the seller object and add the One to many field with the product object
from seller.models import Seller

#Handling file upload paths of images
def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=120, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)#obtain list of objects with respect to the name field(ascending order) 
        verbose_name = 'category'
        verbose_name_plural = 'categories' 

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('category', args=[self.slug])#using view names in URL patterns


""" Add multiple images to the product model using an intermediate model"""
class ImageAlbum(models.Model):
    #You can optionally add the name of the album for easy reference
    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)#One seller has one to many products whereas one product belongs to only one seller
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=150, db_index=True)
    album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE)#This handles uploadnig of multiple images to the product model
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)#This will be the image dipslayed in the all products page
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True) 
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created',)#order product object by if they have been created in descending order
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products-list', args=[self.id, self.slug]) 


class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    review = models.TextField()
   

    def __str__(self):
        return self.name

