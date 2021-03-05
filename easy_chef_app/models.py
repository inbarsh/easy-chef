from django.db import models


class RecipesItem(models.Model):
    objects = None
    content = models.TextField()


class IngredientsItem(models.Model):
    objects = None
    content = models.TextField()


class EquipmentItem(models.Model):
    objects = None
    content = models.TextField()
