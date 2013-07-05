# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Man'
        db.create_table(u'man_man', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('follow_ids', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'man', ['Man'])

        # Adding M2M table for field forward_mans on 'Man'
        m2m_table_name = db.shorten_name(u'man_man_forward_mans')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_man', models.ForeignKey(orm[u'man.man'], null=False)),
            ('to_man', models.ForeignKey(orm[u'man.man'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_man_id', 'to_man_id'])

        # Adding model 'MansLink'
        db.create_table(u'man_manslink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('back', self.gf('django.db.models.fields.related.ForeignKey')(related_name='forward_manslink_set', to=orm['man.Man'])),
            ('forward', self.gf('django.db.models.fields.related.ForeignKey')(related_name='back_manslink_set', to=orm['man.Man'])),
        ))
        db.send_create_signal(u'man', ['MansLink'])

        # Adding unique constraint on 'MansLink', fields ['back', 'forward']
        db.create_unique(u'man_manslink', ['back_id', 'forward_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'MansLink', fields ['back', 'forward']
        db.delete_unique(u'man_manslink', ['back_id', 'forward_id'])

        # Deleting model 'Man'
        db.delete_table(u'man_man')

        # Removing M2M table for field forward_mans on 'Man'
        db.delete_table(db.shorten_name(u'man_man_forward_mans'))

        # Deleting model 'MansLink'
        db.delete_table(u'man_manslink')


    models = {
        u'man.man': {
            'Meta': {'object_name': 'Man'},
            'follow_ids': ('django.db.models.fields.TextField', [], {}),
            'forward_mans': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'back_mans'", 'symmetrical': 'False', 'to': u"orm['man.Man']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'man.manslink': {
            'Meta': {'unique_together': "(('back', 'forward'),)", 'object_name': 'MansLink'},
            'back': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'forward_manslink_set'", 'to': u"orm['man.Man']"}),
            'forward': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'back_manslink_set'", 'to': u"orm['man.Man']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['man']