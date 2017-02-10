# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yallaBlog', '0007_auto_20170210_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='badword',
            old_name='word',
            new_name='rude_word',
        ),
    ]
