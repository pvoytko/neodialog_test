# -*- coding: utf-8 -*-

from django.db import models


# Человек
class Man2(models.Model):
    name = models.CharField(max_length=32)
    follow_ids = models.TextField(blank = True)
    forward_mans = models.ManyToManyField('man.Man2', related_name='back_mans', null = True, blank = True)

    # Выводит число впереди идущих
    @property
    def forward_count(self):
        return self.forward_mans.count()

    # Выводит число сзади идущих
    @property
    def back_count(self):
        return self.back_mans.count()

    # Строковое представление
    def __unicode__(self):
        return u'man.Man#{0} {1}'.format(self.id, self.name)

    class Meta:
        verbose_name = u'Человек'
        verbose_name_plural = u'Люди'

