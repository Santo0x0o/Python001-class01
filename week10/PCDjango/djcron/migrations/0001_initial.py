# Generated by Django 2.2.13 on 2020-09-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_id', models.CharField(max_length=20)),
                ('phone_title', models.CharField(max_length=100)),
                ('phone_url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_id', models.CharField(max_length=20)),
                ('comment_page_id', models.CharField(max_length=4)),
                ('comment_page_url', models.CharField(max_length=50)),
                ('comment_num', models.CharField(max_length=10)),
                ('comment_detail', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_id', models.CharField(max_length=20)),
                ('comment_page_id', models.CharField(max_length=10)),
                ('comment_page_url', models.CharField(max_length=50)),
            ],
        ),
    ]
