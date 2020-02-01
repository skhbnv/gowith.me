from django.db import models


class Categories(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', db_index=True, unique=True)
    category_name = models.CharField(null=True, verbose_name='category_name', max_length=150)


class Users(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', db_index=True, unique=True)
    user_name = models.CharField(verbose_name='user_name', null=True, max_length=150)


class Locations(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', db_index=True, unique=True)
    latitude = models.CharField(verbose_name='latitude', null=True, max_length=250)
    longitude = models.CharField(verbose_name='longitude', null=True, max_length=250)


class Images(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', db_index=True, unique=True)
    poster_url = models.CharField(verbose_name='poster_url', null=True, max_length=150)
    carousel_url1 = models.CharField(verbose_name='poster_url', null=True, max_length=150)
    carousel_url2 = models.CharField(verbose_name='poster_ur2', null=True, max_length=150)
    carousel_url3 = models.CharField(verbose_name='poster_ur3', null=True, max_length=150)
    carousel_url4 = models.CharField(verbose_name='poster_ur4', null=True, max_length=150)
    carousel_url5 = models.CharField(verbose_name='poster_ur5', null=True, max_length=150)


class Events(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id', db_index=True, unique=True)
    date = models.DateTimeField(null=True, verbose_name='date')
    price = models.CharField(verbose_name='price', null=True, max_length=10)
    title = models.CharField(verbose_name='title', null=True, max_length=150)
    category = models.ManyToManyField(Categories, verbose_name='category')
    description = models.CharField(verbose_name='description', null=True, max_length=550)
    location = models.ForeignKey(Locations, max_length=150, null=True, verbose_name='location', on_delete=models.CASCADE)
    images = models.ForeignKey(Images, max_length=150, null=True, verbose_name='images', on_delete=models.CASCADE)

