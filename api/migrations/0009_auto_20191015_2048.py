# Generated by Django 2.2.6 on 2019-10-15 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20191015_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='atvcode',
            new_name='atvname',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='name',
        ),
        migrations.RemoveField(
            model_name='code',
            name='atvcode',
        ),
        migrations.AddField(
            model_name='code',
            name='atvname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Activity'),
        ),
    ]
