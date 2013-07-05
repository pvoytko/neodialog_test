# -*- coding: utf-8 -*-

from django.db import models

class Man(models.Model):
    name = models.CharField(max_length=32)
    follow_ids = models.TextField()
