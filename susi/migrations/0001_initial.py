# Generated by Django 3.0.5 on 2020-06-04 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Susi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, verbose_name='전형명')),
                ('year', models.IntegerField(choices=[(2021, 2021)], verbose_name='학년도')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='susis', to='university.University', verbose_name='대학')),
            ],
            options={
                'verbose_name': '수시전형',
                'verbose_name_plural': '수시전형',
            },
        ),
        migrations.CreateModel(
            name='SusiSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='설명')),
                ('start_date', models.DateTimeField(verbose_name='시작시간')),
                ('end_date', models.DateTimeField(verbose_name='종료시간')),
                ('major_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='susi_schedules', to='university.SusiMajorBlock', verbose_name='학과 블록')),
                ('susi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='susi_schedules', to='susi.Susi', verbose_name='수시전형 종류')),
            ],
            options={
                'verbose_name': '수시전형 일정',
                'verbose_name_plural': '수시전형 일정',
            },
        ),
    ]
