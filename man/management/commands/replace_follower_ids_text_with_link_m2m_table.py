# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.db import models
import man.models


# Старый формат
class Man(models.Model):
    name = models.CharField(max_length=32)
    follow_ids = models.TextField()

    class Meta:
        db_table = "man_man"


# Команда проходит по всей таблице man_man в Джанге.
# И для каждого элемента создает новую запись man_man2.
# С тем же именем. Второй проход вместо followers_id создает связи m2m.
# После чего удаляет запись из man_man.
class Command(BaseCommand):

    def handle(self, *args, **options):

        print "OK"

        # Первый проход - создаем объекты
        for m in Man.objects.all():
            print m.id, m.name
            newM = man.models.Man2(id=m.id, name=m.name)
            newM.save()

        # Второй проход - создаем связи
        for m in Man.objects.all():
            print m.id, m.name, "{0}".format(m.follow_ids),
            if len(m.follow_ids) > 0:
                ids = m.follow_ids.split(' ')
                for id in ids:
                    man.models.Man2.objects.get(id=m.id).forward_mans.add(man.models.Man2.objects.get(id=id))
                print len(ids)
            else:
                print 'skip'