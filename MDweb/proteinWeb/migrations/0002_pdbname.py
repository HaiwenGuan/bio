# Generated by Django 2.2.2 on 2019-07-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteinWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDBName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
