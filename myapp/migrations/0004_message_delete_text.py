# Generated by Django 4.0.5 on 2022-10-31 09:47
#
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('userA', models.CharField(max_length=150)),
                ('userB', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Text',
        ),
    ]
