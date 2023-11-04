# Generated by Django 4.2.6 on 2023-11-04 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_library_app', '0002_alter_siteuser_platform_gamelibrary_gameinlibrary'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamelibrary',
            name='platform',
            field=models.CharField(choices=[('PC', 'Steam'), ('PC', 'Epic Games'), ('PC', 'Battle.net'), ('PC', 'GOG'), ('Console', 'Playstation'), ('Console', 'Xbox'), ('Console', 'Nintendo'), ('Mobile', 'Android'), ('Mobile', 'iOS'), ('Any', 'Any Platform')], default='Any', max_length=50),
        ),
        migrations.AlterField(
            model_name='gameinlibrary',
            name='platform',
            field=models.CharField(choices=[('PC', 'Steam'), ('PC', 'Epic Games'), ('PC', 'Battle.net'), ('PC', 'GOG'), ('Console', 'Playstation'), ('Console', 'Xbox'), ('Console', 'Nintendo'), ('Mobile', 'Android'), ('Mobile', 'iOS'), ('Any', 'Any Platform')], max_length=50),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='platform',
            field=models.CharField(choices=[('PC', 'Steam'), ('PC', 'Epic Games'), ('PC', 'Battle.net'), ('PC', 'GOG'), ('Console', 'Playstation'), ('Console', 'Xbox'), ('Console', 'Nintendo'), ('Mobile', 'Android'), ('Mobile', 'iOS'), ('Any', 'Any Platform')], max_length=50),
        ),
    ]
