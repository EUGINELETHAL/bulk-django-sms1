# Generated by Django 2.2.8 on 2021-01-30 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20190829_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='category',
            field=models.ManyToManyField(related_name='category', to='contacts.Contact_Group'),
        ),
    ]