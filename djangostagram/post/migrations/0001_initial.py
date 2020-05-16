# Generated by Django 3.0.6 on 2020-05-16 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        ('dsuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=512, verbose_name='이미지 주소')),
                ('description', models.TextField(verbose_name='내용')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('tags', models.ManyToManyField(to='tag.Tag', verbose_name='태그')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dsuser.Dsuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '글',
                'verbose_name_plural': '글s',
                'db_table': '글',
                'managed': True,
            },
        ),
    ]
