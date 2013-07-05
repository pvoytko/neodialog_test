# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Man2'
        db.create_table(u'man_man2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('follow_ids', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'man', ['Man2'])

        # Adding M2M table for field forward_mans on 'Man2'
        m2m_table_name = db.shorten_name(u'man_man2_forward_mans')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_man2', models.ForeignKey(orm[u'man.man2'], null=False)),
            ('to_man2', models.ForeignKey(orm[u'man.man2'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_man2_id', 'to_man2_id'])


    def backwards(self, orm):
        # Deleting model 'Man2'
        db.delete_table(u'man_man2')

        # Removing M2M table for field forward_mans on 'Man2'
        db.delete_table(db.shorten_name(u'man_man2_forward_mans'))


    models = {
        u'man.man2': {
            'Meta': {'object_name': 'Man2'},
            'follow_ids': ('django.db.models.fields.TextField', [], {}),
            'forward_mans': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'back_mans'", 'symmetrical': 'False', 'to': u"orm['man.Man2']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['man']