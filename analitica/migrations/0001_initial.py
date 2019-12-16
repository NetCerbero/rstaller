# Generated by Django 2.2.7 on 2019-12-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=16)),
                ('content_id', models.CharField(max_length=16)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('rating_timestamp', models.DateTimeField()),
                ('type', models.CharField(default='explicit', max_length=8)),
            ],
        ),
    ]
