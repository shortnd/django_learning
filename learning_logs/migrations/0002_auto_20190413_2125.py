# Generated by Django 2.2 on 2019-04-13 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.Topic'),
        ),
    ]
