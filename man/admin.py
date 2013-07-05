# -*- coding: utf-8 -*-

from django.contrib import admin
from man.models import Man2
from django import forms

class Man2Form(forms.ModelForm):
    name = forms.CharField(label=u'Имя')
    forward_mans = forms.ModelMultipleChoiceField(queryset=Man2.objects.all(), label=u'Впереди идущие', required=False)
    back_mans = forms.ModelMultipleChoiceField(queryset=Man2.objects.all(), label=u'Позади идущие', required=False)

    def __init__(self, *args, **kwargs):
        super(Man2Form, self).__init__(*args, **kwargs)
        inst = kwargs['instance']
        self.fields['back_mans'].initial = [c.id for c in inst.back_mans.all()]

    def save(self, commit=True):

        # Переопределяем метод save_m2m у формы который используется в Django для сохранения
        # связей и внутри этого метода если заданы предшествователи (сзади идущие), то для каждого из них
        # в последователях сохраняем себя.
        selfMan = super(Man2Form, self).save(commit)
        save_m2m_old = self.save_m2m
        def save_m2m_new():
            if (self.cleaned_data['back_mans']):
                for backMan in self.cleaned_data['back_mans']:
                     backMan.forward_mans.add(selfMan)
            save_m2m_old()
        self.save_m2m = save_m2m_new

        return selfMan


# Возвращает callable объект который можно пердеавать в ModelAdmin.list_display
# имя заголовка в таблице будет columnCaption а в значении будет выводится поле objPropertyName модели.
def displayField(objPropertyName, columnCaption):
    def wrapper(obj):
        return getattr(obj, objPropertyName)
    wrapper.short_description = columnCaption
    return wrapper


# Настройки админки
class Man2Admin(admin.ModelAdmin):
    list_display = (
        displayField('name', u'Имя'),
        displayField('forward_count', u'Кол-во впереди идущих'),
        displayField('back_count', u'Кол-во сзади идущих')
    )
    # fields = ('name', 'forward_mans', 'back_mans')
    form = Man2Form


admin.site.register(Man2, Man2Admin)