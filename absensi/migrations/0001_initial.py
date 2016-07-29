# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('id_kelas', models.CharField(unique=True, max_length=2)),
                ('kelas', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'kelas',
            },
        ),
    ]
