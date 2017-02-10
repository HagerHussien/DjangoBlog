# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yallaBlog', '0005_auto_20170210_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='images/None/no-img.jpg', upload_to=b''),
        ),
    ]
