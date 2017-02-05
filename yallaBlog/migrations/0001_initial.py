# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=200)),
                ('cat', models.ForeignKey(to='yallaBlog.category_table')),
                ('userpost', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
