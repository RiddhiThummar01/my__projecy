# Generated by Django 5.0.6 on 2024-08-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_coursedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='roledata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(max_length=100)),
            ],
        ),
    ]
