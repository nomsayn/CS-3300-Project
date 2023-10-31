# Generated by Django 4.2.6 on 2023-10-27 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('financial_experience', models.CharField(choices=[('Beginner', '0 - 2 years'), ('Advanced', '2 - 5 years'), ('Expert', '5+ years')], max_length=50)),
            ],
        ),
    ]
