# Generated by Django 5.2.3 on 2025-06-28 23:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_picture_contact_show_alter_contact_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures\\%Y\\%m'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.category'),
        ),
    ]
