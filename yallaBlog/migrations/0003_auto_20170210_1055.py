# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yallaBlog', '0002_auto_20170210_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='images/None/no-img.jpg', upload_to='static/images/'),
        ),
    ]
