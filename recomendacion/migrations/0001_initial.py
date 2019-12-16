# Generated by Django 2.2.7 on 2019-12-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeededRecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('source', models.CharField(max_length=16)),
                ('target', models.CharField(max_length=16)),
                ('support', models.DecimalField(decimal_places=8, max_digits=10)),
                ('confidence', models.DecimalField(decimal_places=8, max_digits=10)),
                ('type', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'seeded_recs',
            },
        ),
    ]
