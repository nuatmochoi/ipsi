# Generated by Django 3.0.5 on 2020-05-03 11:37

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='moonigwa',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('MG', '문과'), ('IG', '이과'), ('YCN', '예체능')], max_length=7, verbose_name='계열'),
        ),
    ]